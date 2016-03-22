drop table if exists word_dates;
create table word_dates (
  id integer primary key autoincrement,
  word_string text not null,
  part_of_speech text not null,		 		
  earliest_use text not null
);