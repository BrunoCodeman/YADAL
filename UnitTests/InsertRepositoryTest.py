from Test import Test
from Core.SQLBuilder import SQLBuilder

__author__ = 'logan'

entity = SQLBuilder()

def must_include_all_fields_on_insert_statement():
	"""
	Given an entity
	When I call the insert method
	Then an INSERT SQL command must be generated
	And it must include all the fields of the entity
	"""
	test = Test(1, 2, 3)
	insert = 'INSERT INTO Test (a,b,c) VALUES(1,2,3)'
	generated_insert = entity.insert(test)
	assert insert == generated_insert

def must_replace_none_with_null():
	"""
	Given an entity with
	When I call the insert method
	And one of the properties of the entity has a None value
	Then an INSERT SQL command must be generated
	And it must include all the fields of the entity
	And the None value must be replaced by NULL on the SQL statement
	"""
	test = Test(1, 2, None)
	insert = 'INSERT INTO Test (a,b,c) VALUES(1,2,NULL)'
	generated_insert = entity.insert(test)
	assert insert == generated_insert