from requests_books.status import *

class TestStatus():

    def test_status_code(self):
        s_code = get_status().status_code
        assert get_status().status_code == 200, f'Status code is incorrect. ' \
                                                                 f"Expected status code is 200, but the actual is {s_code}"

    def test_boduy_result(self):
        result = get_status().json()['status']

        assert result == 'OK', f"The status value is not OK. Actual: {result}"
