/* From Flask Tutorial on docs.jinkan.org */

drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title string not null,
	text string not null
);