"""Trilha sonora original sintetizada + efeitos sonoros sincronizados com o vídeo."""
import json, math, os, wave
import numpy as np

SR = 44100
HERE = os.path.dirname(os.path.abspath(__file__))
TL = json.load(open(os.path.join(HERE, 'timeline.json')))
TOTAL = TL['total'] + 0.5
N = int(TOTAL * SR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)

def mf(m): return 440.0 * 2 ** ((m - 69) / 12)

def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N or i + len(sig) <= 0: return
    j = min(N, i + len(sig))
    s = sig[:j - i] * gain
    L[i:j] += s * math.cos((pan + 1) * math.pi / 4) * 1.414
    R[i:j] += s * math.sin((pan + 1) * math.pi / 4) * 1.414

def tt(d): return np.arange(int(d * SR)) / SR

def env_adsr(n, a=0.01, r=0.1):
    e = np.ones(n); na = max(1, int(a * SR)); nr = max(1, min(n, int(r * SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr); return e

# ------------------------------------------------ instrumentos
def piano(m, d):
    f = mf(m); x = tt(d + 0.6); s = np.zeros_like(x)
    for k, a in enumerate([1, .5, .3, .18, .1, .06], 1):
        s += a * np.sin(2 * np.pi * f * k * x * (1 + 0.0004 * k)) * np.exp(-x * (2.2 + k * 0.9))
    e = np.ones_like(x); e[:80] = np.linspace(0, 1, 80)
    n0 = int(d * SR); e[n0:] *= np.exp(-np.arange(len(x) - n0) / SR * 9)
    return s * e * 0.35

def bell(m, d=1.2):
    f = mf(m); x = tt(d)
    s = np.sin(2 * np.pi * f * x) * np.exp(-x * 3) + 0.4 * np.sin(2 * np.pi * f * 3.0 * x) * np.exp(-x * 7) \
        + 0.25 * np.sin(2 * np.pi * f * 4.07 * x) * np.exp(-x * 10)
    s[:40] *= np.linspace(0, 1, 40)
    return s * 0.3

def lead(m, d):
    f = mf(m); x = tt(d)
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * x) * np.clip(x * 3, 0, 1)
    ph = 2 * np.pi * f * np.cumsum(vib) / SR
    s = np.sin(ph) + 0.3 * np.sin(3 * ph) + 0.12 * np.sin(5 * ph) + 0.25 * np.sin(2 * ph)
    return s * env_adsr(len(x), 0.012, min(0.08, d * 0.4)) * np.exp(-x * 1.2) * 0.22

def bass(m, d):
    f = mf(m); x = tt(d)
    s = np.sin(2 * np.pi * f * x) + 0.35 * np.sin(4 * np.pi * f * x) + 0.1 * np.sin(6 * np.pi * f * x)
    return s * env_adsr(len(x), 0.005, 0.05) * np.exp(-x * 2.5) * 0.45

def pad(ms, d, vol=0.08):
    x = tt(d); s = np.zeros_like(x)
    for m in ms:
        f = mf(m)
        for det in (-0.004, 0, 0.004):
            for k in range(1, 6):
                s += np.sin(2 * np.pi * f * k * (1 + det) * x + k) / k ** 1.6
    return s * env_adsr(len(x), min(0.6, d / 3), min(0.8, d / 3)) * vol / len(ms)

def kick():
    x = tt(0.35); f = 50 + 110 * np.exp(-x * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 9) * 0.9

def snare():
    x = tt(0.25)
    return (rng.standard_normal(len(x)) * 0.5 * np.exp(-x * 18) + np.sin(2 * np.pi * 190 * x) * 0.4 * np.exp(-x * 25)) * 0.55

def clap():
    x = tt(0.2); n = rng.standard_normal(len(x))
    e = np.exp(-x * 25) + 0.6 * np.exp(-np.abs(x - 0.012) * 300) + 0.6 * np.exp(-np.abs(x - 0.024) * 300)
    return np.diff(np.concatenate([[0], n])) * e * 0.3

def hat(open_=False):
    x = tt(0.25 if open_ else 0.06); n = rng.standard_normal(len(x))
    return np.diff(np.concatenate([[0], n])) * np.exp(-x * (12 if open_ else 70)) * 0.12

def crash():
    x = tt(2.0); n = rng.standard_normal(len(x))
    return np.diff(np.concatenate([[0], n])) * np.exp(-x * 2.2) * 0.25

def whoosh(d=0.6, up=True):
    n = rng.standard_normal(int(d * SR)); out = np.zeros_like(n); y = 0.0
    for i in range(len(n)):
        p = i / len(n); c = 0.02 + 0.25 * (p if up else 1 - p)
        y += c * (n[i] - y); out[i] = y
    e = np.sin(np.pi * np.arange(len(n)) / len(n)) ** 2
    return out * e * 0.5

def beep(f=1000, d=0.14):
    x = tt(d); return np.sin(2 * np.pi * f * x) * env_adsr(len(x), 0.005, 0.03) * 0.3

def pop():
    x = tt(0.09); f = 950 * np.exp(-x * 25) + 250
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 30) * 0.35

def heartbeat():
    x = tt(0.25); f = 45 + 40 * np.exp(-x * 20)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 14) * 0.9

def sparkle(t0, base=84):
    for i, m in enumerate([0, 4, 7, 12, 16, 19]):
        add(bell(base + m, 1.0), t0 + i * 0.06, 0.5, pan=-0.5 + i * 0.2)

def horn(t0):
    x = tt(0.7); f = 380 + 120 * np.clip(x * 8, 0, 1)
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = sum(np.sin(k * ph) / k for k in range(1, 9)) * env_adsr(len(x), 0.02, 0.15) * 0.12
    add(s, t0)

# ------------------------------------------------ seções
secs = {s['section']: s['start'] for s in TL['scenes'] if s['section']}
BEAT = 0.5  # 120 BPM, compasso = 2 s
CH = {'C': ([60, 64, 67], 36), 'G': ([59, 62, 67], 43), 'Am': ([57, 60, 64], 45), 'F': ([57, 60, 65], 41)}
PROG = ['C', 'G', 'Am', 'F']
MEL = [  # (beat, dur, midi) por compasso
    [(0, 1, 76), (1, .5, 79), (1.5, .5, 76), (2, .5, 74), (2.5, .5, 72), (3, 1, 74)],
    [(0, 1, 74), (1, .5, 79), (1.5, .5, 74), (2, 1, 71), (3, 1, 74)],
    [(0, .5, 72), (.5, .5, 76), (1, 1, 81), (2, .5, 79), (2.5, .5, 76), (3, 1, 72)],
    [(0, 1, 69), (1, 1, 72), (2, 1.5, 77), (3.5, .5, 76)],
    [(0, .5, 76), (.5, .5, 76), (1, 1, 79), (2, 1, 84), (3, 1, 79)],
    [(0, 1, 83), (1, .5, 81), (1.5, .5, 79), (2, 2, 74)],
    [(0, .5, 72), (.5, .5, 76), (1, .5, 81), (1.5, .5, 79), (2, 1, 76), (3, 1, 72)],
    [(0, 1, 77), (1, 1, 76), (2, 1, 74), (3, 1, 72)],
]

def pop_section(t0, t1, tr=0):
    nb = int(round((t1 - t0) / 2))
    for b in range(nb):
        tb = t0 + b * 2; ch, bs = CH[PROG[b % 4]]
        ch = [m + tr for m in ch]; bs += tr
        phrase = (b // 8) % 2  # 0 = com melodia, 1 = sinos/arpejo
        last = b == nb - 1
        # bateria
        for k in (0, 1.5, 2) if b % 2 == 0 else (0, 2, 2.5):
            add(kick(), tb + k * BEAT, 0.9)
        for k in (1, 3):
            add(clap(), tb + k * BEAT, 0.9); add(snare(), tb + k * BEAT, 0.5)
        for k in range(8):
            add(hat(k % 2 == 1 and k == 7), tb + k * 0.25, 0.9 if k % 2 else 0.55, pan=0.3)
        if b % 8 == 7:
            for k in range(8):
                add(snare(), tb + 3 * BEAT + k * BEAT / 8, 0.25 + k * 0.06)
        if b % 8 == 0:
            add(crash(), tb, 0.8, pan=-0.3)
        # baixo
        for k, dd in ((0, .9), (1.5, .4), (2, .9), (3, .4), (3.5, .4)):
            add(bass(bs + (12 if k == 3.5 else 0), dd * BEAT), tb + k * BEAT, 1.0)
        # piano
        for k, dd in ((0, 1.2), (1.5, .8), (3, 1)):
            for m in ch:
                add(piano(m + 12, dd * BEAT), tb + k * BEAT, 0.55, pan=-0.2)
        add(pad(ch, 2.0, 0.06), tb, 1.0)
        if phrase == 0:
            for bt, dd, m in MEL[b % 8]:
                add(lead(m + tr, dd * BEAT), tb + bt * BEAT, 1.0, pan=0.15)
        else:
            arp = ch + [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[0] + 24, ch[2] + 12]
            for k in range(8):
                add(bell(arp[k] + 12, 0.8), tb + k * 0.25, 0.55, pan=-0.4 + 0.1 * k)

def lullaby(t0, t1):
    nb = int(round((t1 - t0) / 2))
    prog = ['C', 'Am', 'F', 'G']
    mel = [[(0, 2, 76), (2, 1, 79), (3, 1, 77)], [(0, 2, 76), (2, 2, 72)], [(0, 2, 77), (2, 1, 76), (3, 1, 74)], [(0, 3, 74), (3, 1, 71)]]
    for b in range(nb):
        tb = t0 + b * 2; ch, bs = CH[prog[b % 4]]
        arp = [ch[0], ch[1], ch[2], ch[0] + 12, ch[2], ch[1], ch[2], ch[0] + 12]
        for k in range(8):
            add(bell(arp[k] + 12, 1.4), tb + k * 0.25, 0.75, pan=-0.3 + 0.08 * k)
        add(pad(ch + [bs + 12], 2.1, 0.15), tb, 1.0)
        add(bass(bs, 1.6), tb, 0.55)
        if b >= 2:
            for bt, dd, m in mel[b % 4]:
                add(bell(m + 12, dd * BEAT + 1.0), tb + bt * BEAT, 1.0, pan=0.2)

def intro():
    add(pad([48, 55, 60, 64], 6.0, 0.12), 0.0)
    for k in range(4):
        add(np.sin(2 * np.pi * 2000 * tt(0.02)) * np.exp(-tt(0.02) * 200) * 0.25, k * 0.5)  # tic-tac
    for k in (2, 3, 4):
        add(beep(1000), k)
    add(beep(2000, 0.35), 5.0, 1.2)
    sparkle(5.0, 79)
    add(whoosh(1.2, True), 4.8, 0.7)

def happy_birthday(t0):
    b = 60 / 132
    mel = [(67, .75), (67, .25), (69, 1), (67, 1), (72, 1), (71, 2), (67, .75), (67, .25), (69, 1), (67, 1), (74, 1), (72, 2),
           (67, .75), (67, .25), (79, 1), (76, 1), (72, 1), (71, 1), (69, 1), (77, .75), (77, .25), (76, 1), (72, 1), (74, 1), (72, 3)]
    chords = ['C', 'G', 'G', 'C', 'C', 'F', 'G', 'C']
    end = t0
    for rep in range(2):
        tr = t0 + rep * 25 * b
        t = tr
        for m, d in mel:
            add(lead(m + 12 * rep, d * b * 0.95), t, 1.1, pan=0.1)
            if rep == 1: add(bell(m + 12, 1.0), t, 0.35)
            t += d * b
        for i, c in enumerate(chords):
            tb = tr + b + i * 3 * b
            ch, bs = CH[c]
            add(bass(bs, b * 0.9), tb, 1.0); add(kick(), tb, 0.7)
            for k in (1, 2):
                for m in ch: add(piano(m + 12, b * 0.6), tb + k * b, 0.45)
                add(hat(), tb + k * b, 0.8)
            if rep == 1: add(clap(), tb + 2 * b, 0.8)
            add(pad(ch, 3 * b, 0.05), tb, 1.0)
        end = t
    # acorde final
    for m in (48, 60, 64, 67, 72, 76):
        add(piano(m, 3.0), end, 0.6)
    add(pad([60, 64, 67, 72], TOTAL - end, 0.08), end, 1.0)
    add(crash(), end, 0.8)
    sparkle(end, 84)

intro()
pop_section(secs['popA'], secs['lullaby'])
lullaby(secs['lullaby'], secs['popB'])
pop_section(secs['popB'], secs['finale'], tr=2)
add(crash(), secs['popB'], 0.8)
happy_birthday(secs['finale'])
horn(secs['finale'] + 0.05)
add(crash(), secs['finale'], 0.9)

# ------------------------------------------------ efeitos por cena
for s in TL['scenes']:
    t0 = s['start']
    if t0 == 0: continue
    tr = s['trans']
    if tr in ('slide', 'zoom', 'circle', 'heart'):
        add(whoosh(0.5, True), t0 - 0.05, 0.35, pan=0.3 if tr == 'slide' else 0)
    elif tr == 'flash':
        add(whoosh(0.3, False), t0 - 0.1, 0.25)
    elif tr == 'balloons':
        add(whoosh(1.2, True), t0, 0.5)
    if s['type'] == 'title':
        add(pop(), t0 + 0.25, 0.7); sparkle(t0 + 0.3, 88)
    if s['type'] == 'photo' and s['entry'] == 'drop':
        add(pop(), t0 + 0.32, 0.5)
    if s['type'] == 'stork':
        add(whoosh(1.5, True), t0 + 0.5, 0.4, pan=-0.6); add(whoosh(1.5, False), t0 + 2.0, 0.4, pan=0.6)
        sparkle(t0 + 0.3, 84); sparkle(t0 + 2.4, 88)
    if s['type'] == 'birthcard':
        for k in range(4):
            add(heartbeat(), t0 + 0.6 + k * 0.85, 0.8); add(heartbeat(), t0 + 0.6 + k * 0.85 + 0.22, 0.6)
    if s['type'] == 'info':
        for i in range(4): add(pop(), t0 + 1.0 + i * 0.35, 0.6)
        sparkle(t0 + 2.8, 84)
    if s['type'] == 'end':
        sparkle(t0 + 0.5, 84)

# ------------------------------------------------ mixagem
mix = np.stack([L, R], 1)
mix /= np.percentile(np.abs(mix), 99.95) + 1e-9
mix = np.tanh(mix * 0.9) * 0.92
fade = int(2.0 * SR)
mix[-fade:] *= np.linspace(1, 0, fade)[:, None]
pcm = (mix * 32767).astype(np.int16)
with wave.open(os.path.join(HERE, 'trilha.wav'), 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok', TOTAL)
