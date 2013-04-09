from Test import Test
from Core.SQLBuilder import SQLBuilder

__author__ = 'logan'

entity = SQLBuilder()


def must_generate_delete_without_params():
    """
    Given an entity
    When I call the delete method without the where_clause parameter
    Then it must return a DELETE SQL statement without a where clause
    """
    test = Test(1, 2, 3)
    delete = 'DELETE FROM Test '
    delete_statement = entity.delete(test)
    assert delete == delete_statement


must_generate_delete_without_params()


def must_generate_delete_with_params():
    """
    Given and entity
    When I call the delete method with the where_clause parameter
    Then it must return a DELETE SQL statement with a where clause
    """
    test = Test(1, 2, 3)
    delete = 'DELETE FROM Test WHERE a = 5 AND b = 6'
    delete_statement = entity.delete(test, where_clause=dict(a=5, b=6))
    assert delete == delete_statement

must_generate_delete_with_params()