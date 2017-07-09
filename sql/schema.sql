drop table if exists profile;
create table profile (
  id integer primary key autoincrement,
  name string not null,
  pwd string not null,
  student_id string not null
);