create extension vector;
create table runbooks (content text, embeddings vector(1536));
create index on runbooks using hnsw (embeddings vector_cosine_ops);