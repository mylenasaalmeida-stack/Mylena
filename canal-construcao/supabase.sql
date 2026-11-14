-- Cole no Supabase: SQL Editor > New query > Run
create table if not exists public.pedidos (
  id          bigint generated always as identity primary key,
  criado_em   timestamptz not null default now(),
  numero      text not null,
  cliente     jsonb not null,   -- nome, telefone, e-mail
  entrega     jsonb not null,   -- modo de envio e endereço
  pagamento   text not null,
  itens       jsonb not null,   -- lista de produtos, quantidades e preços
  total       numeric(12,2),
  status      text not null default 'novo'
);

alter table public.pedidos enable row level security;

-- O site (chave anon) só pode CRIAR pedidos. Ler, editar e apagar fica
-- restrito ao painel do Supabase (ou a usuários autenticados da loja).
drop policy if exists "site cria pedidos" on public.pedidos;
create policy "site cria pedidos" on public.pedidos
  for insert to anon with check (true);
