from Test import Test
from Core.SQLBuilder import SQLBuilder

__author__ = 'logan'

entity = SQLBuilder()


def must_generate_update_without_params():
    """
    Given an entity
    When I call the update method without the where_clause parameter
    Then it must return an UPDATE SQL statement without a where clause
    """
    test = Test(1, 2, 3)
    update_statement = 'UPDATE Teste SET a = 1, b = 2, c = 3'
    update = entity.update(test)
    assert update == update_statement

