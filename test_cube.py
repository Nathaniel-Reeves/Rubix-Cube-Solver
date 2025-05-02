import pytest
import random as r
from cube import Cube
from cube import Facet
import random

# Use pytest-spec
# pytest --spec

todo = pytest.mark.skip(reason="TODO: Not implemented yet.")

def describe_cube():
    
    @pytest.fixture
    def mock_r(mocker):
        mock_r = mocker.patch.object(Cube, 'r', return_value=None)
        return mock_r
    
    @pytest.fixture
    def mock_rp(mocker):
        mock_rp = mocker.patch.object(Cube, 'rp', return_value=None)
        return mock_rp
    
    @pytest.fixture
    def mock_f(mocker):
        mock_f = mocker.patch.object(Cube, 'f', return_value=None)
        return mock_f
    
    @pytest.fixture
    def mock_fp(mocker):
        mock_fp = mocker.patch.object(Cube, 'fp', return_value=None)
        return mock_fp
    
    @pytest.fixture
    def mock_l(mocker):
        mock_l = mocker.patch.object(Cube, 'l', return_value=None)
        return mock_l
    
    @pytest.fixture
    def mock_lp(mocker):
        mock_lp = mocker.patch.object(Cube, 'lp', return_value=None)
        return mock_lp
    
    @pytest.fixture
    def mock_b(mocker):
        mock_b = mocker.patch.object(Cube, 'b', return_value=None)
        return mock_b
    
    @pytest.fixture
    def mock_bp(mocker):
        mock_bp = mocker.patch.object(Cube, 'bp', return_value=None)
        return mock_bp
    
    @pytest.fixture
    def mock_u(mocker):
        mock_u = mocker.patch.object(Cube, 'u', return_value=None)
        return mock_u
    
    @pytest.fixture
    def mock_up(mocker):
        mock_up = mocker.patch.object(Cube, 'up', return_value=None)
        return mock_up
    
    @pytest.fixture
    def mock_d(mocker):
        mock_d = mocker.patch.object(Cube, 'd', return_value=None)
        return mock_d
    
    @pytest.fixture
    def mock_dp(mocker):
        mock_dp = mocker.patch.object(Cube, 'dp', return_value=None)
        return mock_dp
    
    @pytest.fixture
    def mock_moves(mock_r, mock_rp, mock_f, mock_fp, mock_l, mock_lp, mock_b, mock_bp, mock_u, mock_up, mock_d, mock_dp):
        return { 'r': mock_r, 'rp': mock_rp, 'f': mock_f, 'fp': mock_fp, 'l': mock_l, 'lp': mock_lp, 'b': mock_b, 'bp': mock_bp, 'u': mock_u, 'up': mock_up, 'd': mock_d, 'dp': mock_dp }
    
    @pytest.fixture
    def red_facets():
        return { 'bl': 3, 'b_': 6, 'br': 9, '_l': 12, 'mm': 15, '_r': 18, 'tl': 21, 't_': 24, 'tr': 27 }
    
    @pytest.fixture
    def blue_facets():
        return { 'bl': 1, 'b_': 2, 'br': 3, '_l': 10, 'mm': 11, '_r': 12, 'tl': 19, 't_': 20, 'tr': 21 }
    
    @pytest.fixture
    def orange_facets():
        return { 'bl': 7, 'b_': 4, 'br': 1, '_l': 16, 'mm': 13, '_r': 10, 'tl': 25, 't_': 22, 'tr': 19 }
    
    @pytest.fixture
    def green_facets():
        return { 'bl': 9, 'b_': 8, 'br': 7, '_l': 18, 'mm': 17, '_r': 16, 'tl': 27, 't_': 26, 'tr': 25 }
    
    @pytest.fixture
    def yellow_facets():
        return { 'bl': 19, 'b_': 20, 'br': 21, '_l': 22, 'mm': 23, '_r': 24, 'tl': 25, 't_': 26, 'tr': 27 }
    
    @pytest.fixture
    def white_facets():
        return { 'bl': 7, 'b_': 8, 'br': 9, '_l': 4, 'mm': 5, '_r': 6, 'tl': 1, 't_': 2, 'tr': 3 }
    
    @pytest.fixture
    def faces(red_facets, blue_facets, orange_facets, green_facets, yellow_facets, white_facets):
        return { 'red': red_facets, 'blue': blue_facets, 'orange': orange_facets, 'green': green_facets, 'yellow': yellow_facets, 'white': white_facets }
    
    def describe_init():
        
        def it_returns_instance():
            c = Cube()
            assert isinstance(c, Cube)
    
    def describe_manipulating_the_cube():
        
        def it_can_be_mixed_up_and_solved():
            c = Cube()
            assert c.solved() == True
            
            moves = [
                "R", "R'",
                "F", "F'",
                "L", "L'",
                "B", "B'",
                "U", "U'",
                "D", "D'"
            ]
            stack = []
            
            for i in range(50):
                move = r.choice(moves)
                stack.append(move)
            
            for move in stack:
                c.do_move(move)
            
            assert c.solved() == False
            print()
            
            stack.reverse()
            
            for move in stack:
                c.do_reverse_move(move)
            
            assert c.solved() == True

    def describe_valid_moves():
        
        def it_returns_a_list():
            c = Cube()
            l = c.get_valid_moves()
            assert isinstance(l, list)
        
        def it_returns_a_12_item_long_list():
            c = Cube()
            l = c.get_valid_moves()
            assert len(l) == 12
        
        def it_returns_the_correct_moves():
            correct_moves = ["R", "R'", "F", "F'", "L", "L'", "B", "B'", "U", "U'", "D", "D'"]
            c = Cube()
            l = c.get_valid_moves()
            assert set(l) == set(correct_moves)
    
    def describe_check_valid_move():
        
        def it_accepts_a_move():
            c = Cube()
            move = 'R'
            out = c.check_valid_move(move)
            assert out == True
        
        def it_raises_a_value_error_with_message_for_a_invalid_move():
            c = Cube()
            move = 'invalid move'
            with pytest.raises(ValueError) as e_info:
                c.check_valid_move(move)
                assert e_info.message == 'Invalid move: %s' % move
    
    def describe_do_move():
        
        def it_accepts_a_move():
            c = Cube()
            move = 'R'
            out = c.do_move(move)
            assert out == True
        
        def it_raises_a_value_error_with_message_for_a_invalid_move():
            c = Cube()
            move = 'invalid move'
            with pytest.raises(ValueError) as e_info:
                c.do_move(move)
                assert e_info.message == 'Invalid move: %s' % move
        
        def it_calls_the_r_move(mock_moves):
            c = Cube()
            mock_r = mock_moves['r']
            c.do_move("R")
            mock_r.assert_called_once()
        
        def it_calls_the_rp_move(mock_moves):
            c = Cube()
            mock_rp = mock_moves['rp']
            c.do_move("R'")
            mock_rp.assert_called_once()
        
        def it_calls_the_f_move(mock_moves):
            c = Cube()
            mock_f = mock_moves['f']
            c.do_move("F")
            mock_f.assert_called_once()
        
        def it_calls_the_fp_move(mock_moves):
            c = Cube()
            mock_fp = mock_moves['fp']
            c.do_move("F'")
            mock_fp.assert_called_once()
        
        def it_calls_the_l_move(mock_moves):
            c = Cube()
            mock_l = mock_moves['l']
            c.do_move("L")
            mock_l.assert_called_once()
        
        def it_calls_the_lp_move(mock_moves):
            c = Cube()
            mock_lp = mock_moves['lp']
            c.do_move("L'")
            mock_lp.assert_called_once()
        
        def it_calls_the_b_move(mock_moves):
            c = Cube()
            mock_b = mock_moves['b']
            c.do_move("B")
            mock_b.assert_called_once()
        
        def it_calls_the_bp_move(mock_moves):
            c = Cube()
            mock_bp = mock_moves['bp']
            c.do_move("B'")
            mock_bp.assert_called_once()
        
        def it_calls_the_u_move(mock_moves):
            c = Cube()
            mock_u = mock_moves['u']
            c.do_move("U")
            mock_u.assert_called_once()
        
        def it_calls_the_up_move(mock_moves):
            c = Cube()
            mock_up = mock_moves['up']
            c.do_move("U'")
            mock_up.assert_called_once()
        
        def it_calls_the_d_move(mock_moves):
            c = Cube()
            mock_d = mock_moves['d']
            c.do_move("D")
            mock_d.assert_called_once()
        
        def it_calls_the_dp_move(mock_moves):
            c = Cube()
            mock_dp = mock_moves['dp']
            c.do_move("D'")
            mock_dp.assert_called_once()
    
    def describe_do_reverse_move():
        
        def it_accepts_a_move():
            c = Cube()
            move = 'R'
            out = c.do_reverse_move(move)
            assert out == True
        
        def it_raises_a_value_error_with_message_for_a_invalid_move():
            c = Cube()
            move = 'invalid move'
            with pytest.raises(ValueError) as e_info:
                c.do_reverse_move(move)
                assert e_info.message == 'Invalid move: %s' % move
        
        def it_calls_the_reverse_of_the_r_move(mock_moves):
            c = Cube()
            mock_rp = mock_moves['rp']
            c.do_reverse_move("R")
            mock_rp.assert_called_once()
        
        def it_calls_the_reverse_of_the_rp_move(mock_moves):
            c = Cube()
            mock_r = mock_moves['r']
            c.do_reverse_move("R'")
            mock_r.assert_called_once()
        
        def it_calls_the_reverse_of_the_f_move(mock_moves):
            c = Cube()
            mock_fp = mock_moves['fp']
            c.do_reverse_move("F")
            mock_fp.assert_called_once()
        
        def it_calls_the_reverse_of_the_fp_move(mock_moves):
            c = Cube()
            mock_f = mock_moves['f']
            c.do_reverse_move("F'")
            mock_f.assert_called_once()
        
        def it_calls_the_reverse_of_the_l_move(mock_moves):
            c = Cube()
            mock_lp = mock_moves['lp']
            c.do_reverse_move("L")
            mock_lp.assert_called_once()
        
        def it_calls_the_reverse_of_the_lp_move(mock_moves):
            c = Cube()
            mock_l = mock_moves['l']
            c.do_reverse_move("L'")
            mock_l.assert_called_once()
        
        def it_calls_the_reverse_of_the_b_move(mock_moves):
            c = Cube()
            mock_bp = mock_moves['bp']
            c.do_reverse_move("B")
            mock_bp.assert_called_once()
        
        def it_calls_the_reverse_of_the_bp_move(mock_moves):
            c = Cube()
            mock_b = mock_moves['b']
            c.do_reverse_move("B'")
            mock_b.assert_called_once()
        
        def it_calls_the_reverse_of_the_u_move(mock_moves):
            c = Cube()
            mock_up = mock_moves['up']
            c.do_reverse_move("U")
            mock_up.assert_called_once()
        
        def it_calls_the_reverse_of_the_up_move(mock_moves):
            c = Cube()
            mock_u = mock_moves['u']
            c.do_reverse_move("U'")
            mock_u.assert_called_once()
        
        def it_calls_the_reverse_of_the_d_move(mock_moves):
            c = Cube()
            mock_dp = mock_moves['dp']
            c.do_reverse_move("D")
            mock_dp.assert_called_once()
        
        def it_calls_the_reverse_of_the_dp_move(mock_moves):
            c = Cube()
            mock_d = mock_moves['d']
            c.do_reverse_move("D'")
            mock_d.assert_called_once()
    
    def describe_solved():
        
        def it_returns_true_when_all_facets_are_solved():
            c = Cube()
            out = c.solved()
            assert out == True
        
        def it_returns_false_when_at_least_one_facet_is_not_solved():
            c = Cube()
            vl = c.get_valid_moves()
            
            c = Cube()
            move = random.choice(vl)
            c.do_move(move)
            out = c.solved()
            assert out == False
            
            c = Cube()
            move = random.choice(vl)
            c.do_move(move)
            out = c.solved()
            assert out == False
            
            c = Cube()
            move = random.choice(vl)
            c.do_move(move)
            out = c.solved()
            assert out == False
            
            c = Cube()
            move = random.choice(vl)
            c.do_move(move)
            out = c.solved()
            assert out == False
            
            c = Cube()
            move = random.choice(vl)
            c.do_move(move)
            out = c.solved()
            assert out == False
    
    def describe_r():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "R"
            face = "red"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'w'
                assert facet.get_ba() == 'y'
                assert facet.get_t()  == 'b'
                assert facet.get_bo() == 'g'
                assert facet.get_l()  == 'o'
                assert facet.get_r()  == 'r'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "R"
            face = "red"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_rp():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "R'"
            face = "red"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'y'
                assert facet.get_ba() == 'w'
                assert facet.get_t()  == 'g'
                assert facet.get_bo() == 'b'
                assert facet.get_l()  == 'o'
                assert facet.get_r()  == 'r'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "R'"
            face = "red"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_f():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "F"
            face = "blue"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'b'
                assert facet.get_ba() == 'g'
                assert facet.get_t()  == 'o'
                assert facet.get_bo() == 'r'
                assert facet.get_l()  == 'w'
                assert facet.get_r()  == 'y'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "F"
            face = "blue"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_fp():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "F'"
            face = "blue"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'b'
                assert facet.get_ba() == 'g'
                assert facet.get_t()  == 'r'
                assert facet.get_bo() == 'o'
                assert facet.get_l()  == 'y'
                assert facet.get_r()  == 'w'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "F'"
            face = "blue"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_l():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "L"
            face = "orange"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'y'
                assert facet.get_ba() == 'w'
                assert facet.get_t()  == 'g'
                assert facet.get_bo() == 'b'
                assert facet.get_l()  == 'o'
                assert facet.get_r()  == 'r'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "L"
            face = "orange"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_lp():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "L'"
            face = "orange"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'w'
                assert facet.get_ba() == 'y'
                assert facet.get_t()  == 'b'
                assert facet.get_bo() == 'g'
                assert facet.get_l()  == 'o'
                assert facet.get_r()  == 'r'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "L'"
            face = "orange"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_b():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "B"
            face = "green"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'b'
                assert facet.get_ba() == 'g'
                assert facet.get_t()  == 'r'
                assert facet.get_bo() == 'o'
                assert facet.get_l()  == 'y'
                assert facet.get_r()  == 'w'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "B"
            face = "green"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_bp():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "B'"
            face = "green"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'b'
                assert facet.get_ba() == 'g'
                assert facet.get_t()  == 'o'
                assert facet.get_bo() == 'r'
                assert facet.get_l()  == 'w'
                assert facet.get_r()  == 'y'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "B'"
            face = "green"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_u():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "U"
            face = "yellow"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'r'
                assert facet.get_ba() == 'o'
                assert facet.get_t()  == 'y'
                assert facet.get_bo() == 'w'
                assert facet.get_l()  == 'b'
                assert facet.get_r()  == 'g'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "U"
            face = "yellow"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_up():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "U'"
            face = "yellow"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'o'
                assert facet.get_ba() == 'r'
                assert facet.get_t()  == 'y'
                assert facet.get_bo() == 'w'
                assert facet.get_l()  == 'g'
                assert facet.get_r()  == 'b'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "U'"
            face = "yellow"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_d():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "D"
            face = "white"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'o'
                assert facet.get_ba() == 'r'
                assert facet.get_t()  == 'y'
                assert facet.get_bo() == 'w'
                assert facet.get_l()  == 'g'
                assert facet.get_r()  == 'b'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "D"
            face = "white"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    def describe_dp():
        
        def it_rotates_the_correct_facets_correclty(faces):
            move = "D'"
            face = "white"
            
            c = Cube()
            c.do_move(move)
            
            for position, facet_index in faces[face].items():
                facet = c.get_facet(facet_index)
                assert facet.get_f()  == 'r'
                assert facet.get_ba() == 'o'
                assert facet.get_t()  == 'y'
                assert facet.get_bo() == 'w'
                assert facet.get_l()  == 'b'
                assert facet.get_r()  == 'g'
        
        def it_does_nothing_to_the_other_facets(faces):
            move = "D'"
            face = "white"
            
            c = Cube()

            # Get other facets not on specified face.
            specified_facet_indexes = faces[face].values()
            facet_indexes = [ item for item in range(1, 27+1) ]

            for remove_index in specified_facet_indexes:
                facet_indexes.remove(remove_index)

            # Get Facets that should not be manipulated by test.
            test_facets = {}
            for index in facet_indexes:
                test_facets[index] = c.get_facet(index)

            c.do_move(move)
            
            # Ensure that Facets that shouls not be manipulated
            # were not manipulated by test.
            for facet_index in test_facets.keys():
                facet = c.get_facet(facet_index)
                assert facet.solved() == True
    
    @todo
    def describe__str__():
        pass
    
def describe_facet():
    
    def describe_init_and_getters():
        
        def it_returns_instance():
            f = Facet('1')
            assert isinstance(f, Facet)
        
        def it_sets_default_colors():
            f = Facet('1')
            assert f.get_f() == 'b'
            assert f.get_ba() == 'g'
            assert f.get_t() == 'y'
            assert f.get_bo() == 'w'
            assert f.get_l() == 'o'
            assert f.get_r() == 'r'
    
    def describe_solved():
        
        def it_should_return_true_when_solved():
            f = Facet('1')
            assert f.solved() == True
            
        def it_should_return_false_when_not_solved():
            f = Facet('1')
            f.left_color = 'b'
            f.right_color = 'g'
            assert f.solved() == False
            
    def describe_x_axis_rotation():
        
        def it_should_turn_facet_clockwise():
            f = Facet('1')
            f.rx()
            assert f.get_f() == 'w'
            assert f.get_ba() == 'y'
            assert f.get_t() == 'b'
            assert f.get_bo() == 'g'
            assert f.get_l() == 'o'
            assert f.get_r() == 'r'
            
        def it_should_turn_facet_counter_clockwise():
            f = Facet('1')
            f.rxp()
            assert f.get_f() == 'y'
            assert f.get_ba() == 'w'
            assert f.get_t() == 'g'
            assert f.get_bo() == 'b'
            assert f.get_l() == 'o'
            assert f.get_r() == 'r'
        
    def describe_y_axis_rotation():
        
        def it_should_turn_facet_clockwise():
            f = Facet('1')
            f.ry()
            assert f.get_f() == 'r'
            assert f.get_ba() == 'o'
            assert f.get_t() == 'y'
            assert f.get_bo() == 'w'
            assert f.get_l() == 'b'
            assert f.get_r() == 'g'
        
        def it_should_turn_facet_counter_clockwise():
            f = Facet('1')
            f.ryp()
            assert f.get_f() == 'o'
            assert f.get_ba() == 'r'
            assert f.get_t() == 'y'
            assert f.get_bo() == 'w'
            assert f.get_l() == 'g'
            assert f.get_r() == 'b'
    
    def describe_z_axis_rotation():
        
        def it_should_turn_facet_clockwise():
            f = Facet('1')
            f.rz()
            assert f.get_f() == 'b'
            assert f.get_ba() == 'g'
            assert f.get_t() == 'o'
            assert f.get_bo() == 'r'
            assert f.get_l() == 'w'
            assert f.get_r() == 'y'
        
        def it_should_turn_facet_counter_clockwise():
            f = Facet('1')
            f.rzp()
            assert f.get_f() == 'b'
            assert f.get_ba() == 'g'
            assert f.get_t() == 'r'
            assert f.get_bo() == 'o'
            assert f.get_l() == 'y'
            assert f.get_r() == 'w'