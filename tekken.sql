create database Tekken7

go

use Tekken7

go

create table characters
(
	id int primary key identity(1, 1),
	title nvarchar(100),
	wikiTitle nvarchar(100),
	rbTitle nvarchar(100),
	fightingStyle nvarchar(100),
	origin nvarchar(100),
	heightCm int,
	weightKg int,
	gender char check(gender in ('m', 'f', 'a'))
)

create table charcterRelationships
(
	characterId int foreign key references characters(id),
	parentId int foreign key references characters(id),
	primary key (characterId, parentId)
)

create table moves
(
	id int primary key identity(1, 1),
	characterId int foreign key references characters(id),
	input nvarchar(50),
	startup nvarchar(100),
	damage int
)
