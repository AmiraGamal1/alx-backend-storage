-- create index for first letter on name

CREATE INDEX idx_name_first
ON names(name(1));