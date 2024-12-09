import pytest
from brute import Brute
from unittest.mock import Mock
from unittest.mock import patch

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    
    # @patch('brute')

    def describe_bruteOnce():
        # write your test cases here
        def it_returns_true_if_correct():
            brute = Brute("testing string")
            assert brute.bruteOnce("testing string") == True

        def it_fails_if_first_brute_is_not_correct():
            brute = Brute("testing string")
            assert brute.bruteOnce("wrong") == False

        def it_only_tests_once():
            with patch.object(Brute, 'bruteOnce') as mock_brute:
                thing = Brute("testing string")
                thing.bruteOnce("testing string")
            mock_brute.assert_called_once()
            

    def describe_bruteMany():
        # write your test cases here
        def it_runs_without_crashing():
            brute = Brute("hello")
            assert brute.bruteMany(10) == -1

        def it_returns_the_time_when_successful():
            brute = Brute("a")
            assert brute.bruteMany(10000000) != -1

        def it_tests_many_times():
            with patch.object(Brute, 'bruteMany') as mock_brute:
                thing = Brute("testing string")
                thing.bruteMany("testing string")
            mock_brute.assert_called_once()
