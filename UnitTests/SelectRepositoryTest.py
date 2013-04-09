from Test import Test
from Core.SQLBuilder import SQLBuilder

__author__ = 'logan'

entity = SQLBuilder()

def must_return_select():
	"""
	Given an entity
	when I call the select method
	And don't specify fields nor where clause
	Then I must see a simples SELECT command
	"""
	test = Test(1, 2, 3)
	query = 'SELECT a, b, c FROM Test '
	select_query = entity.select(test)
	assert query == select_query

must_return_select()


def must_return_select_with_defined_fields():
	"""
	Given an entity
	when I call the select method
	And specify fields, but not where clause
	Then I must see a SELECT command with the specified fields
	"""
	test = Test(1, 2, 3)
	query = 'SELECT a, b FROM Test '
	select_query = entity.select(test, fields=['a', 'b'])
	assert query == select_query

must_return_select_with_defined_fields()


def must_replace_none_with_null_on_select():
	"""
	Given an entity
	when I call the select method
	And specify fields, and the where clause
	And one of the values on where clause is None
	Then I must see a SELECT command with the specified fields
	And the '= None' must be replaced with 'IS NULL' on the select command
	"""
	test = Test(1, 2, None)
	query = 'SELECT a, b FROM Test WHERE a = 1 AND c IS NULL AND b = 2'
	select_query = entity.select(test, fields=['a', 'b'], where_clause=dict(a=1, b=2, c=None))
	assert query == select_query

must_replace_none_with_null_on_select()


def must_return_select_with_specific_where_clause():
	"""
	Given an entity
	when I call the select method
	And specify the where clause, but not the fields
	Then the WHERE clause of my SELECT command must match the fields and values passed as parameters
	"""
	test = Test(1, 2, 3)
	query = 'SELECT a, b, c FROM Test WHERE a = 5 AND b = 4'
	select_query = entity.select(test, where_clause={'a': 5, 'b': 4})
	assert query == select_query

must_return_select_with_specific_where_clause()