#coding: utf-8
__author__ = 'logan'


class Entity():

	def __init__(self):
		self.__query = 'SELECT %s FROM %s '
		self.__insert = 'INSERT INTO %s (%s) VALUES(%s)'
		self.__delete = 'DELETE FROM % '
		pass

	def select(self, entity, fields=[], where_clause={}):
		columns = ', '.join(fields) if len(fields) > 0 else ', '.join([property for property in vars(entity).keys()])
		table = entity.__class__.__name__
		where_clause = where_clause if len(where_clause) > 0 else vars(entity)
		and_string = ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()])

		self.__query = self.__query % (columns, table)

		self.__query += ' WHERE ' + and_string

		self.__query = self.__query.replace(' = None', ' IS NULL')

		return self.__query

	def insert(self, entity):
		columns = ', '.join([property for property in vars(entity).keys()])
		values = ', '.join([str(property) for property in vars(entity).values()])
		table = entity.__class__.__name__
		self.__insert = self.__insert % (table, columns, values)
		return self.__insert.replace('None', ' NULL ')


	def delete(self, entity, where_clause):
		table = entity.__class__.__name__
		where_string = ' WHERE '.join(['%s = %s' % (k, v) for k, v in where_clause.items()[:1]])
		and_clause = '' if len(where_clause) < 2 else ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()[1:]])

		self.__delete = self.__delete % (table, where_string)
		return  self.__delete + and_clause