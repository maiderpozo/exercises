from contextlib import contextmanager
from scripting.testing import test
from scripting.quick import reference_based_test
from scripting.reference import active_reference_implementation_from_id, reference_file


with reference_file('solution.py'):
    with reference_based_test('square') as testcase:
        testcase(0)
        testcase(1)
        testcase(2)
        testcase(3)
        testcase(-1)
        testcase(-2)

         