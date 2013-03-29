#coding: utf-8
__author__ = 'logan'
import operator

class Entity():

	def __init__(self):
		self.__query = 'SELECT %s FROM %s '
		self.__insert = 'INSERT INTO %s (%s) VALUES(%s)'
		self.__delete = 'DELETE FROM % '
		pass

	def select(self, entity, fields=[], where_clause={}):
		"""
		Build a string with a SELECT command.
		:param entity: an object of a class
		:param fields: list of strings. Each string must be a column name
		:param where_clause: dictionary where the keys are column names and values are the matching values
		"""

		columns = ', '.join(fields) if any(fields) else ', '.join([property for property in sorted(vars(entity).keys())])
		table = entity.__class__.__name__
		where_clause = where_clause if any(where_clause) else sorted(vars(entity).iteritems(), key=operator.itemgetter(1))
		and_string = ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()]) if where_clause.__class__ is dict \
						else ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause])

		query = self.__query % (columns, table)

		query += 'WHERE %s' % and_string

		query = query.replace(' = None', ' IS NULL')

		return query

	def insert(self, entity):
		columns = ', '.join([property for property in vars(entity).keys()])
		values = ', '.join([str(property) for property in vars(entity).values()])
		table = entity.__class__.__name__
		self.__insert = self.__insert % (table, columns, values)
		return self.__insert.replace('None', ' NULL ')


	def delete(self, entity, where_clause):
		"""

		:param entity: Entity to delete
		:param where_clause: dictionary with parameters to the SQL expression
		:return: string with the DELETE command formatted
		"""
		table = entity.__class__.__name__
		where_string =  ' WHERE '.join(['%s = %s' % (k, v) for k, v in where_clause.items()[:1]])\
						if any(where_clause.items()) else ''

		and_clause = '' if len(where_clause) < 2 else ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()[1:]])

		self.__delete = self.__delete % table
		return  (self.__delete + where_string + and_clause).replace(' = None ',' IS NULL ' )