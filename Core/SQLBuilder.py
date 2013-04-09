#coding: utf-8
__author__ = 'logan'
import operator


class SQLBuilder():
    def __init__(self):
        self.__query = 'SELECT %s FROM %s '
        self.__insert = 'INSERT INTO %s (%s) VALUES(%s)'
        self.__delete = 'DELETE FROM %s '
        self.__update = 'UPDATE %s SET %s'
        pass

    def select(self, entity, fields=[], where_clause={}):
        """
		Build a string with a SELECT command.
		:param entity: an object of a class
		:param fields: list of strings. Each string must be a column name
		:param where_clause: dictionary where the keys are column names and values are the matching values
		"""
        and_string = ''
        columns = ', '.join(fields) if any(fields) else ', '.join(
            [property for property in sorted(vars(entity).keys())])
        table = entity.__class__.__name__
        if any(where_clause): and_string = 'WHERE %s' % ' AND '.join(
            ['%s = %s' % (k, v) for k, v in where_clause.items()])

        query = self.__query % (columns, table)

        query += and_string

        query = query.replace(' = None', ' IS NULL')

        return query

    def insert(self, entity):
        """
		Returns a INSERT SQL statement generated based on the entity

		:param entity: The entity to be inserted on database
		"""
        columns = ', '.join([property for property in vars(entity).keys()])
        values = ', '.join([str(property) for property in vars(entity).values()])
        table = entity.__class__.__name__
        insert_string = self.__insert % (table, columns, values)
        return insert_string.replace('None', ' NULL ')


    def delete(self, entity, where_clause={}):
        """
		Return a DELETE SQL statement
		:param entity: Entity to delete
		:param where_clause: dictionary with parameters to the SQL expression
		:return: string with the DELETE command formatted
		"""
        table = entity.__class__.__name__
        and_string = 'WHERE %s' % ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()]) if any(
            where_clause) else ''
        delete_string = self.__delete % table
        delete_string += and_string
        return delete_string.replace('None', 'NULL')


def update(self, entity, where_clause={}):
    """

    :param self:
    :param entity:
    :param where_clause:
    :return:
    """
    table = entity.__class__.__name__
    and_string = 'WHERE %s' % ' AND '.join(['%s = %s' % (k, v) for k, v in where_clause.items()]) if any(
        where_clause) else ''
    set_clause = ','.join(['%s = %s' % (k, v) for k, v in vars(entity).items()])
    update_string = self.__update % table
    update_string += set_clause + and_string
    return update_string.replace('None','Null')