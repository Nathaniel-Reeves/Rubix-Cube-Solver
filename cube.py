import random
from kociembas import solve, solve_best

class Cube:
    """Representation of a 3x3x3 Cube"""
    
    def __init__(self):
        
        self.cube = {
            '1': Facet('1'), #1 Front Bottom Left of Cube
            '2': Facet('2'), #2
            '3': Facet('3'), #3
            '4': Facet('4'), #4
            '5': Facet('5'), #5
            '6': Facet('6'), #6
            '7': Facet('7'), #7
            '8': Facet('8'), #8
            '9': Facet('9'), #9
            '10': Facet('10'), #10
            '11': Facet('11'), #11
            '12': Facet('12'), #12
            '13': Facet('13'), #13
            '14': Facet('14'), #14 Center of Cube
            '15': Facet('15'), #15
            '16': Facet('16'), #16
            '17': Facet('17'), #17
            '18': Facet('18'), #18
            '19': Facet('19'), #19
            '20': Facet('20'), #20
            '21': Facet('21'), #21
            '22': Facet('22'), #22
            '23': Facet('23'), #23
            '24': Facet('24'), #24
            '25': Facet('25'), #25
            '26': Facet('26'), #26
            '27': Facet('27')  #27 Back Top Right of Cube
        }
        
        self.red_facets    = { 'bl': '3',  'b_': '6',  'br': '9',  '_l': '12', 'mm': '15', '_r': '18', 'tl': '21', 't_': '24', 'tr': '27' }
        self.blue_facets   = { 'bl': '1',  'b_': '2',  'br': '3',  '_l': '10', 'mm': '11', '_r': '12', 'tl': '19', 't_': '20', 'tr': '21' }
        self.orange_facets = { 'bl': '7',  'b_': '4',  'br': '1',  '_l': '16', 'mm': '13', '_r': '10', 'tl': '25', 't_': '22', 'tr': '19' }
        self.green_facets  = { 'bl': '9',  'b_': '8',  'br': '7',  '_l': '18', 'mm': '17', '_r': '16', 'tl': '27', 't_': '26', 'tr': '25' }
        self.yellow_facets = { 'bl': '19', 'b_': '20', 'br': '21', '_l': '22', 'mm': '23', '_r': '24', 'tl': '25', 't_': '26', 'tr': '27' }
        self.white_facets  = { 'bl': '7',  'b_': '8',  'br': '9',  '_l': '4',  'mm': '5',  '_r': '6',  'tl': '1',  't_': '2',  'tr': '3' }
        
        self.faces = { 'red': self.red_facets, 'blue': self.blue_facets, 'orange': self.orange_facets, 'green': self.green_facets, 'yellow': self.yellow_facets, 'white': self.white_facets }
    
    def _prepare_cube_string(self):
        # Front
        face = 'front_color'
        f1 = f"{getattr(self.cube['19'], face)}{getattr(self.cube['20'], face)}{getattr(self.cube['21'], face)}"
        f2 = f"{getattr(self.cube['10'], face)}{getattr(self.cube['11'], face)}{getattr(self.cube['12'], face)}"
        f3 = f"{getattr(self.cube['1'], face)}{getattr(self.cube['2'], face)}{getattr(self.cube['3'], face)}"
        f = f1 + f2 + f3
        
        # Left
        face = 'left_color'
        l1 = f"{getattr(self.cube['25'], face)}{getattr(self.cube['22'], face)}{getattr(self.cube['19'], face)}"
        l2 = f"{getattr(self.cube['16'], face)}{getattr(self.cube['13'], face)}{getattr(self.cube['10'], face)}"
        l3 = f"{getattr(self.cube['7'], face)}{getattr(self.cube['4'], face)}{getattr(self.cube['1'], face)}"
        l = l1 + l2 + l3
        
        # Right
        face = 'right_color'
        r1 = f"{getattr(self.cube['21'], face)}{getattr(self.cube['24'], face)}{getattr(self.cube['27'], face)}"
        r2 = f"{getattr(self.cube['12'], face)}{getattr(self.cube['15'], face)}{getattr(self.cube['18'], face)}"
        r3 = f"{getattr(self.cube['3'], face)}{getattr(self.cube['6'], face)}{getattr(self.cube['9'], face)}"
        r = r1 + r2 + r3
        
        # Top
        face = 'top_color'
        t1 = f"{getattr(self.cube['25'], face)}{getattr(self.cube['26'], face)}{getattr(self.cube['27'], face)}"
        t2 = f"{getattr(self.cube['22'], face)}{getattr(self.cube['23'], face)}{getattr(self.cube['24'], face)}"
        t3 = f"{getattr(self.cube['19'], face)}{getattr(self.cube['20'], face)}{getattr(self.cube['21'], face)}"
        u = t1 + t2 + t3
        
        # Bottom
        face = 'bottom_color'
        bo1 = f"{getattr(self.cube['1'], face)}{getattr(self.cube['2'], face)}{getattr(self.cube['3'], face)}"
        bo2 = f"{getattr(self.cube['4'], face)}{getattr(self.cube['5'], face)}{getattr(self.cube['6'], face)}"
        bo3 = f"{getattr(self.cube['7'], face)}{getattr(self.cube['8'], face)}{getattr(self.cube['9'], face)}"
        d = bo1 + bo2 + bo3
        
        # Back
        face = 'back_color'
        ba1 = f"{getattr(self.cube['27'], face)}{getattr(self.cube['26'], face)}{getattr(self.cube['25'], face)}"
        ba2 = f"{getattr(self.cube['18'], face)}{getattr(self.cube['17'], face)}{getattr(self.cube['16'], face)}"
        ba3 = f"{getattr(self.cube['9'], face)}{getattr(self.cube['8'], face)}{getattr(self.cube['7'], face)}"
        b = ba1 + ba2 + ba3
        
        out = u + r + f + d + l + b
        
        key = {
            'y': 'U',
            'w': 'D',
            'b': 'F',
            'g': 'B',
            'r': 'R',
            'o': 'L'
        }
        
        cube_string = ''
        for c in out:
            cube_string += key[c]
        return cube_string
        
    
    def get_solution(self):
        cube_string = self._prepare_cube_string()
        return solve(cube_string)
    
    def get_best_solution(self):
        cube_string = self._prepare_cube_string()
        solutions = solve_best(cube_string)
        for i, solution in enumerate(solutions):
            print(f'Solution #{i+1} :',solution)
            print()
    
    def _get_face(self, center_color):
        text = ''
        top_color = ''
        left_color = ''
        right_color = ''
        bottom_color = ''

        if center_color == 'w':
            text = 'White'
            top_color = 'B'
            left_color = 'O'
            right_color = 'R'
            bottom_color = 'G'
        elif center_color == 'y':
            text = 'Yellow'
            top_color = 'G'
            left_color = 'O'
            right_color = 'R'
            bottom_color = 'B'
        elif center_color == 'g':
            text = 'Green'
            top_color = 'W'
            left_color = 'O'
            right_color = 'R'
            bottom_color = 'Y'
        elif center_color == 'b':
            text = 'Blue'
            top_color = 'Y'
            left_color = 'O'
            right_color = 'R'
            bottom_color = 'W'
        elif center_color == 'r':
            text = 'Red'
            top_color = 'Y'
            left_color = 'B'
            right_color = 'G'
            bottom_color = 'W'
        elif center_color == 'o':
            text = 'Orange'
            top_color = 'Y'
            left_color = 'G'
            right_color = 'B'
            bottom_color = 'W'
        else:
            raise ValueError(center_color, " Is an invalid color.")
        
        while True:
            print()
            print(text, "Face")
            print(f"     {top_color}")
            print(f"   {left_color} {text[0]} {right_color}")
            print(f"     {bottom_color}")
            print()
            l1 = input("Row1 :")
            l2 = input("Row2 :")
            l3 = input("Row3 :")
            print()
            face = l1 + l2 + l3
            flag = True
            for l in face:
                if l not in ['w','y','g','b','r','o']:
                    flag = False
            if (l2[1] == center_color and 
                len(l1) == 3 and 
                len(l2) == 3 and 
                len(l3) == 3 and flag):
                print("Entered Face is Valid.")
                print()
                return face
            else:
                print("Invalid Cube Face, Try Again.")
                print()
    
    def _validate_cube_string(self, string):
        if (string.count('w') == 9 and
            string.count('r') == 9 and
            string.count('b') == 9 and
            string.count('g') == 9 and
            string.count('y') == 9 and
            string.count('o') == 9 and
            len(string) == 54
        ):
            return True
        return False
    
    def _get_custom_cube(self):
        faces = ['y','b','r','o','g','w']
        while True:
            custom_cube_input_data = {}
            validate = ''
            print("Read in color values from right to")
            print("left for each row. Only use the   ")
            print("following values for each color:  ")
            print("   White:  'w'")
            print("   Red:    'r'")
            print("   Blue:   'b'")
            print("   Green:  'g'")
            print("   Yellow: 'y'")
            print("   Orange: 'o'")
            
            for face in faces:
                data = self._get_face(face)
                validate += data
                custom_cube_input_data[face] = data
                
            if (self._validate_cube_string(validate)):
                print("Entered Cube is Valid.")
                print()
                return custom_cube_input_data
            else:
                print("Entered Cube is not valid!")
                print("Try Again.")
                print()
    
    def build_custom_cube(self):
        data = self._get_custom_cube()
        cube = {}
        for i in range(1, 28, 1):
            new_f = Facet(str(i))
            f = self._set_facet(new_f, data)
            cube[str(i)] = f
        self._set_cube(cube)
    
    def _set_facet(self, f, data):
        if f.get_id() == '1':
            f_c = data['b'][6]
            l_c = data['o'][8]
            b_c = data['w'][0]
            f.set_facet(front=f_c,left=l_c,bottom=b_c)
        elif f.get_id() == '2':
            f_c = data['b'][7]
            b_c = data['w'][1]
            f.set_facet(front=f_c,bottom=b_c)
        elif f.get_id() == '3':
            f_c = data['b'][8]
            r_c = data['r'][6]
            b_c = data['w'][2]
            f.set_facet(front=f_c,right=r_c,bottom=b_c)
        elif f.get_id() == '4':
            l_c = data['o'][7]
            b_c = data['w'][3]
            f.set_facet(left=l_c,bottom=b_c)
        elif f.get_id() == '6':
            r_c = data['r'][7]
            b_c = data['w'][5]
            f.set_facet(right=r_c,bottom=b_c)
        elif f.get_id() == '7':
            b_c = data['w'][6]
            ba_c = data['g'][0]
            l_c = data['o'][6]
            f.set_facet(bottom=b_c,back=ba_c,left=l_c)
        elif f.get_id() == '8':
            b_c = data['w'][7]
            ba_c = data['g'][1]
            f.set_facet(bottom=b_c,back=ba_c)
        elif f.get_id() == '9':
            b_c = data['w'][8]
            r_c = data['r'][8]
            ba_c = data['g'][2]
            f.set_facet(bottom=b_c,right=r_c,back=ba_c)
        elif f.get_id() == '10':
            f_c = data['b'][3]
            l_c = data['o'][5]
            f.set_facet(front=f_c,left=l_c)
        elif f.get_id() == '12':
            f_c = data['b'][5]
            r_c = data['r'][3]
            f.set_facet(front=f_c,right=r_c)
        elif f.get_id() == '16':
            l_c = data['o'][3]
            b_c = data['g'][3]
            f.set_facet(left=l_c,back=b_c)
        elif f.get_id() == '18':
            r_c = data['r'][5]
            b_c = data['g'][5]
            f.set_facet(right=r_c,back=b_c)
        elif f.get_id() == '19':
            f_c = data['b'][0]
            t_c = data['y'][6]
            l_c = data['o'][2]
            f.set_facet(front=f_c,top=t_c,left=l_c)
        elif f.get_id() == '20':
            f_c = data['b'][1]
            t_c = data['y'][7]
            f.set_facet(front=f_c,top=t_c)
        elif f.get_id() == '21':
            f_c = data['b'][2]
            t_c = data['y'][8]
            r_c = data['r'][0]
            f.set_facet(front=f_c,top=t_c,right=r_c)
        elif f.get_id() == '22':
            t_c = data['y'][3]
            l_c = data['o'][1]
            f.set_facet(top=t_c,left=l_c)
        elif f.get_id() == '24':
            t_c = data['y'][5]
            r_c = data['r'][1]
            f.set_facet(top=t_c,right=r_c)
        elif f.get_id() == '25':
            t_c = data['y'][0]
            l_c = data['o'][0]
            b_c = data['g'][6]
            f.set_facet(top=t_c,left=l_c,back=b_c)
        elif f.get_id() == '26':
            t_c = data['y'][1]
            b_c = data['g'][7]
            f.set_facet(top=t_c,back=b_c)
        elif f.get_id() == '27':
            t_c = data['y'][2]
            r_c = data['r'][2]
            b_c = data['g'][8]
            f.set_facet(top=t_c,right=r_c,back=b_c)
        return f
    
    def _set_cube(self, cube_data):
        self.cube = cube_data
        print("New Cube Set: ")
        print()
        print(self)
    
    def get_facet(self, index):
        if str(index) in self.cube.keys():
            return self.cube[str(index)]
        else:
            raise ValueError("Cube Index %d not found." % index)
    
    def get_valid_moves(self):
        return ["R", "R'", "F", "F'", "L", "L'", "B", "B'", "U", "U'", "D", "D'"]
    
    def check_valid_move(self, move):
        moves = self.get_valid_moves()
        if move not in moves:
            raise ValueError("Invalid move: %s" % move)
        return True
    
    def do_move(self, move):
        self.check_valid_move(move)
        if move == "R":
            self.r()
        elif move == "R'":
            self.rp()
        elif move == "F":
            self.f()
        elif move == "F'":
            self.fp()
        elif move == "L":
            self.l()
        elif move == "L'":
            self.lp()
        elif move == "B":
            self.b()
        elif move == "B'":
            self.bp()
        elif move == "U":
            self.u()
        elif move == "U'":
            self.up()
        elif move == "D":
            self.d()
        else:
            self.dp()
        return True
    
    def do_reverse_move(self, move):
        self.check_valid_move(move)
        if move == "R":
            self.rp()
        elif move == "R'":
            self.r()
        elif move == "F":
            self.fp()
        elif move == "F'":
            self.f()
        elif move == "L":
            self.lp()
        elif move == "L'":
            self.l()
        elif move == "B":
            self.bp()
        elif move == "B'":
            self.b()
        elif move == "U":
            self.up()
        elif move == "U'":
            self.u()
        elif move == "D":
            self.dp()
        else:
            self.d()
        return True
    
    def solved(self):
        for i in self.cube:
            if not self.cube[i].solved():
                return False
            # if self.cube[i].get_id() != str(i):
            #     return False
        return True
    
    def r(self):
        print("R")
        
        #     ->
        # 21  24  27
        # 12  15  18
        #  3   6   9
        #     <-
        
        # Rotate Corners
        temp = self.cube['9']
        self.cube['9'] = self.cube['27']
        self.cube['27'] = self.cube['21']
        self.cube['21'] = self.cube['3']
        self.cube['3'] = temp

        # Rotate Edges
        temp = self.cube['18']
        self.cube['18'] = self.cube['24']
        self.cube['24'] = self.cube['12']
        self.cube['12'] = self.cube['6']
        self.cube['6'] = temp
        
        # Rotate Facets
        self.cube['3'].rx()
        self.cube['6'].rx()
        self.cube['9'].rx()
        self.cube['12'].rx()
        self.cube['15'].rx()
        self.cube['18'].rx()
        self.cube['21'].rx()
        self.cube['24'].rx()
        self.cube['27'].rx()
    
    def rp(self):
        print("R'")
        
        #     <-
        # 21  24  27
        # 12  15  18
        #  3   6   9
        #     ->
        
        # Rotate Corners
        temp = self.cube['21']
        self.cube['21'] = self.cube['27']
        self.cube['27'] = self.cube['9']
        self.cube['9'] = self.cube['3']
        self.cube['3'] = temp

        # Rotate Edges
        temp = self.cube['12']
        self.cube['12'] = self.cube['24']
        self.cube['24'] = self.cube['18']
        self.cube['18'] = self.cube['6']
        self.cube['6'] = temp
        
        # Rotate Facets
        self.cube['3'].rxp()
        self.cube['6'].rxp()
        self.cube['9'].rxp()
        self.cube['12'].rxp()
        self.cube['15'].rxp()
        self.cube['18'].rxp()
        self.cube['21'].rxp()
        self.cube['24'].rxp()
        self.cube['27'].rxp()
    
    def f(self):
        print("F")
        
        #     ->
        # 19  20  21
        # 10  11  12
        #  1   2   3
        #     <-
        
        # Rotate Corners
        temp = self.cube['3']
        self.cube['3'] = self.cube['21']
        self.cube['21'] = self.cube['19']
        self.cube['19'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['12']
        self.cube['12'] = self.cube['20']
        self.cube['20'] = self.cube['10']
        self.cube['10'] = self.cube['2']
        self.cube['2'] = temp

        # Rotate Facets
        self.cube['1'].rz()
        self.cube['2'].rz()
        self.cube['3'].rz()
        self.cube['10'].rz()
        self.cube['11'].rz()
        self.cube['12'].rz()
        self.cube['19'].rz()
        self.cube['20'].rz()
        self.cube['21'].rz()
    
    def fp(self):
        print("F'")
        
        #     <-
        # 19  20  21
        # 10  11  12
        #  1   2   3
        #     ->
        
        # Rotate Corners
        temp = self.cube['19']
        self.cube['19'] = self.cube['21']
        self.cube['21'] = self.cube['3']
        self.cube['3'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['10']
        self.cube['10'] = self.cube['20']
        self.cube['20'] = self.cube['12']
        self.cube['12'] = self.cube['2']
        self.cube['2'] = temp

        # Rotate Facets
        self.cube['1'].rzp()
        self.cube['2'].rzp()
        self.cube['3'].rzp()
        self.cube['10'].rzp()
        self.cube['11'].rzp()
        self.cube['12'].rzp()
        self.cube['19'].rzp()
        self.cube['20'].rzp()
        self.cube['21'].rzp()
    
    def l(self):
        print("L")
        
        #     ->
        # 25  22  19
        # 16  13  10
        #  7   4   1
        #     <-
        
        # Rotate Corners
        temp = self.cube['19']
        self.cube['19'] = self.cube['25']
        self.cube['25'] = self.cube['7']
        self.cube['7'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['22']
        self.cube['22'] = self.cube['16']
        self.cube['16'] = self.cube['4']
        self.cube['4'] = self.cube['10']
        self.cube['10'] = temp

        # Rotate Facets
        self.cube['1'].rxp()
        self.cube['4'].rxp()
        self.cube['7'].rxp()
        self.cube['10'].rxp()
        self.cube['13'].rxp()
        self.cube['16'].rxp()
        self.cube['19'].rxp()
        self.cube['22'].rxp()
        self.cube['25'].rxp()
    
    def lp(self):
        print("L'")
        
        #     <-
        # 25  22  19
        # 16  13  10
        #  7   4   1
        #     ->
        
        # Rotate Corners
        temp = self.cube['7']
        self.cube['7'] = self.cube['25']
        self.cube['25'] = self.cube['19']
        self.cube['19'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['4']
        self.cube['4'] = self.cube['16']
        self.cube['16'] = self.cube['22']
        self.cube['22'] = self.cube['10']
        self.cube['10'] = temp

        # Rotate Facets
        self.cube['1'].rx()
        self.cube['4'].rx()
        self.cube['7'].rx()
        self.cube['10'].rx()
        self.cube['13'].rx()
        self.cube['16'].rx()
        self.cube['19'].rx()
        self.cube['22'].rx()
        self.cube['25'].rx()
    
    def b(self):
        print("B")
        
        #     ->
        # 27  26  25
        # 18  17  16
        #  9   8   7
        #     <-
        
        # Rotate Corners
        temp = self.cube['25']
        self.cube['25'] = self.cube['27']
        self.cube['27'] = self.cube['9']
        self.cube['9'] = self.cube['7']
        self.cube['7'] = temp

        # Rotate Edges
        temp = self.cube['16']
        self.cube['16'] = self.cube['26']
        self.cube['26'] = self.cube['18']
        self.cube['18'] = self.cube['8']
        self.cube['8'] = temp

        # Rotate Facets
        self.cube['7'].rzp()
        self.cube['8'].rzp()
        self.cube['9'].rzp()
        self.cube['16'].rzp()
        self.cube['17'].rzp()
        self.cube['18'].rzp()
        self.cube['25'].rzp()
        self.cube['26'].rzp()
        self.cube['27'].rzp()
    
    def bp(self):
        print("B'")
        
        #     <-
        # 27  26  25
        # 18  17  16
        #  9   8   7
        #     ->
        
        # Rotate Corners
        temp = self.cube['27']
        self.cube['27'] = self.cube['25']
        self.cube['25'] = self.cube['7']
        self.cube['7'] = self.cube['9']
        self.cube['9'] = temp

        # Rotate Edges
        temp = self.cube['18']
        self.cube['18'] = self.cube['26']
        self.cube['26'] = self.cube['16']
        self.cube['16'] = self.cube['8']
        self.cube['8'] = temp

        # Rotate Facets
        self.cube['7'].rz()
        self.cube['8'].rz()
        self.cube['9'].rz()
        self.cube['16'].rz()
        self.cube['17'].rz()
        self.cube['18'].rz()
        self.cube['25'].rz()
        self.cube['26'].rz()
        self.cube['27'].rz()
    
    def u(self):
        print("U")
        
        #     ->
        # 25  26  27
        # 22  23  24
        # 19  20  21
        #     <-
        
        # Rotate Corners
        temp = self.cube['21']
        self.cube['21'] = self.cube['27']
        self.cube['27'] = self.cube['25']
        self.cube['25'] = self.cube['19']
        self.cube['19'] = temp

        # Rotate Edges
        temp = self.cube['24']
        self.cube['24'] = self.cube['26']
        self.cube['26'] = self.cube['22']
        self.cube['22'] = self.cube['20']
        self.cube['20'] = temp

        # Rotate Facets
        self.cube['19'].ry()
        self.cube['20'].ry()
        self.cube['21'].ry()
        self.cube['22'].ry()
        self.cube['23'].ry()
        self.cube['24'].ry()
        self.cube['25'].ry()
        self.cube['26'].ry()
        self.cube['27'].ry()

    def up(self):
        print("U'")
        
        #     <-
        # 25  26  27
        # 22  23  24
        # 19  20  21
        #     ->
        
        # Rotate Corners
        temp = self.cube['25']
        self.cube['25'] = self.cube['27']
        self.cube['27'] = self.cube['21']
        self.cube['21'] = self.cube['19']
        self.cube['19'] = temp

        # Rotate Edges
        temp = self.cube['22']
        self.cube['22'] = self.cube['26']
        self.cube['26'] = self.cube['24']
        self.cube['24'] = self.cube['20']
        self.cube['20'] = temp

        # Rotate Facets
        self.cube['19'].ryp()
        self.cube['20'].ryp()
        self.cube['21'].ryp()
        self.cube['22'].ryp()
        self.cube['23'].ryp()
        self.cube['24'].ryp()
        self.cube['25'].ryp()
        self.cube['26'].ryp()
        self.cube['27'].ryp()
    
    def d(self):
        print("D")
        
        #     ->
        #  1   2   3
        #  4   5   6
        #  7   8   9
        #     <-
        
        # Rotate Corners
        temp = self.cube['7']
        self.cube['7'] = self.cube['9']
        self.cube['9'] = self.cube['3']
        self.cube['3'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['4']
        self.cube['4'] = self.cube['8']
        self.cube['8'] = self.cube['6']
        self.cube['6'] = self.cube['2']
        self.cube['2'] = temp

        # Rotate Facets
        self.cube['1'].ryp()
        self.cube['2'].ryp()
        self.cube['3'].ryp()
        self.cube['4'].ryp()
        self.cube['5'].ryp()
        self.cube['6'].ryp()
        self.cube['7'].ryp()
        self.cube['8'].ryp()
        self.cube['9'].ryp()
    
    def dp(self):
        print("D'")
        
        #     <-
        #  1   2   3
        #  4   5   6
        #  7   8   9
        #     ->
        
        # Rotate Corners
        temp = self.cube['3']
        self.cube['3'] = self.cube['9']
        self.cube['9'] = self.cube['7']
        self.cube['7'] = self.cube['1']
        self.cube['1'] = temp

        # Rotate Edges
        temp = self.cube['6']
        self.cube['6'] = self.cube['8']
        self.cube['8'] = self.cube['4']
        self.cube['4'] = self.cube['2']
        self.cube['2'] = temp

        # Rotate Facets
        self.cube['1'].ry()
        self.cube['2'].ry()
        self.cube['3'].ry()
        self.cube['4'].ry()
        self.cube['5'].ry()
        self.cube['6'].ry()
        self.cube['7'].ry()
        self.cube['8'].ry()
        self.cube['9'].ry()
    
    def __str__(self):
        
        # Front
        c = 'blue'
        face = 'front_color'
        f1 = f"{getattr(self.cube[self.faces[c]['tl']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tr']], face)}"
        f2 = f"{getattr(self.cube[self.faces[c]['_l']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_r']], face)}"
        f3 = f"{getattr(self.cube[self.faces[c]['bl']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['br']], face)}"
        
        # Left
        c = 'orange'
        face = 'left_color'
        l1 = f"{getattr(self.cube[self.faces[c]['tl']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tr']], face)}"
        l2 = f"{getattr(self.cube[self.faces[c]['_l']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_r']], face)}"
        l3 = f"{getattr(self.cube[self.faces[c]['bl']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['br']], face)}"
        
        # Right
        c = 'red'
        face = 'right_color'
        r1 = f"{getattr(self.cube[self.faces[c]['tl']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tr']], face)}"
        r2 = f"{getattr(self.cube[self.faces[c]['_l']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_r']], face)}"
        r3 = f"{getattr(self.cube[self.faces[c]['bl']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['br']], face)}"
        
        # Top
        c = 'yellow'
        face = 'top_color'
        t1 = f"{getattr(self.cube[self.faces[c]['tl']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tr']], face)}"
        t2 = f"{getattr(self.cube[self.faces[c]['_l']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_r']], face)}"
        t3 = f"{getattr(self.cube[self.faces[c]['bl']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['br']], face)}"
        
        # Bottom
        c = 'white'
        face = 'bottom_color'
        bo1 = f"{getattr(self.cube[self.faces[c]['tl']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tr']], face)}"
        bo2 = f"{getattr(self.cube[self.faces[c]['_l']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_r']], face)}"
        bo3 = f"{getattr(self.cube[self.faces[c]['bl']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['br']], face)}"
        
        # Back
        c = 'green'
        face = 'back_color'
        ba1 = f"{getattr(self.cube[self.faces[c]['br']], face)} {getattr(self.cube[self.faces[c]['b_']], face)} {getattr(self.cube[self.faces[c]['bl']], face)}"
        ba2 = f"{getattr(self.cube[self.faces[c]['_r']], face)} {getattr(self.cube[self.faces[c]['mm']], face)} {getattr(self.cube[self.faces[c]['_l']], face)}"
        ba3 = f"{getattr(self.cube[self.faces[c]['tr']], face)} {getattr(self.cube[self.faces[c]['t_']], face)} {getattr(self.cube[self.faces[c]['tl']], face)}"
        
        # Stich Strings Together
        out = ' '*7 + t1 + '\n'
        out += ' '*7 + t2 + '\n'
        out += ' '*7 + t3 + '\n'
        out += '\n'
        out += l1 + '  ' + f1 + '  ' + r1 + '\n'
        out += l2 + '  ' + f2 + '  ' + r2 + '\n'
        out += l3 + '  ' + f3 + '  ' + r3 + '\n'
        out += '\n'
        out += ' '*7 + bo1 + '\n'
        out += ' '*7 + bo2 + '\n'
        out += ' '*7 + bo3 + '\n'
        out += '\n'
        out += ' '*7 + ba1 + '\n'
        out += ' '*7 + ba2 + '\n'
        out += ' '*7 + ba3 + '\n'
        return out
    
class Facet:
    
    def __init__(self, id):
        """Initalizes the Facet"""
        self.top_color = 'y'
        self.bottom_color = 'w'
        self.left_color = 'o'
        self.right_color = 'r'
        self.front_color = 'b'
        self.back_color = 'g'
        self.id = id
    
    def get_id(self):
        return self.id
    
    def __eq__(self, other):
        return (self.id == other.id)
    
    def __str__(self):
        return f'<Facet id:{self.id} f:{self.front_color} ba:{self.back_color} t:{self.top_color} bo:{self.bottom_color} r:{self.right_color} l:{self.left_color}>'
    
    def get_f(self):
        return self.front_color
    
    def get_ba(self):
        return self.back_color
    
    def get_t(self):
        return self.top_color
    
    def get_bo(self):
        return self.bottom_color
    
    def get_l(self):
        return self.left_color
    
    def get_r(self):
        return self.right_color
    
    def set_facet(self, front='_', back='_', left='_', right='_', top='_', bottom='_'):
        # Set inital colors
        self.front_color = front
        self.back_color = back
        self.left_color = left
        self.right_color = right
        self.top_color = top
        self.bottom_color = bottom
        
        # Set parallel pairs
        def set_parallel_pairs(self):
            parallel_pairs = {
                'w':'y',
                'y':'w',
                'g':'b',
                'b':'g',
                'r':'o',
                'o':'r'
            }
            if self.front_color == '_' and self.back_color != '_':
                self.front_color = parallel_pairs[self.back_color]
            if self.back_color == '_' and self.front_color != '_':
                self.back_color = parallel_pairs[self.front_color]
            if self.left_color == '_' and self.right_color != '_':
                self.left_color = parallel_pairs[self.right_color]
            if self.right_color == '_' and self.left_color != '_':
                self.right_color = parallel_pairs[self.left_color]
            if self.top_color == '_' and self.bottom_color != '_':
                self.top_color = parallel_pairs[self.bottom_color]
            if self.bottom_color == '_' and self.top_color != '_':
                self.bottom_color = parallel_pairs[self.top_color]
            
        def set_y_axis_adjacent_pairs(self):
            adjacent_pairs = {
                'o':'g',
                'b':'r',
                'g':'o',
                'r':'b',
                'w':'_',
                'y':'_'
            }
            if self.front_color == '_' and self.left_color != '_':
                self.front_color = adjacent_pairs[self.left_color]
            if self.back_color == '_' and self.right_color != '_':
                self.back_color = adjacent_pairs[self.right_color]
            if self.left_color == '_' and self.back_color != '_':
                self.left_color = adjacent_pairs[self.back_color]
            if self.right_color == '_' and self.front_color != '_':
                self.right_color = adjacent_pairs[self.front_color]
        
        def set_x_axis_adjacent_pairs(self):
            adjacent_pairs = {
                'w':'r',
                'r':'y',
                'y':'o',
                'o':'w',
                'b':'_',
                'g':'_'
            }
            if self.front_color == '_' and self.top_color != '_':
                self.front_color = adjacent_pairs[self.top_color]
            if self.bottom_color == '_' and self.front_color != '_':
                self.bottom_color = adjacent_pairs[self.front_color]
            if self.back_color == '_' and self.bottom_color != '_':
                self.back_color = adjacent_pairs[self.bottom_color]
            if self.top_color == '_' and self.back_color != '_':
                self.top_color = adjacent_pairs[self.back_color]

        set_parallel_pairs(self)
        set_x_axis_adjacent_pairs(self)
        set_y_axis_adjacent_pairs(self)
        set_parallel_pairs(self)
        return 
        
    def solved(self):
        return (
            self.top_color == 'y' and
            self.bottom_color == 'w' and
            self.left_color == 'o' and
            self.right_color == 'r' and
            self.front_color == 'b' and
            self.back_color == 'g'
        )
    
    def rx(self):
        """Rotate x plane Clockwise"""
        temp = self.back_color
        self.back_color = self.top_color
        self.top_color = self.front_color
        self.front_color = self.bottom_color
        self.bottom_color = temp
    
    def rxp(self):
        """Rotate x plane Counter-Clockwise"""
        temp = self.back_color
        self.back_color = self.bottom_color
        self.bottom_color = self.front_color
        self.front_color = self.top_color
        self.top_color = temp
    
    def ry(self):
        """Rotate y plate Clockwise"""
        temp = self.back_color
        self.back_color = self.left_color
        self.left_color = self.front_color
        self.front_color = self.right_color
        self.right_color = temp
    
    def ryp(self):
        """Rotate y plane Counter-Clockwise"""
        temp = self.back_color
        self.back_color = self.right_color
        self.right_color = self.front_color
        self.front_color = self.left_color
        self.left_color = temp
    
    def rz(self):
        """Rotate z plane Clockwise"""
        temp = self.bottom_color
        self.bottom_color = self.right_color
        self.right_color = self.top_color
        self.top_color = self.left_color
        self.left_color = temp
    
    def rzp(self):
        """Rotate z plane Counter-Clockwise"""
        temp = self.bottom_color
        self.bottom_color = self.left_color
        self.left_color = self.top_color
        self.top_color = self.right_color
        self.right_color = temp
    
    def __str__(self):
        return f'<Facet ID:{self.id} f:{self.front_color} ba:{self.back_color} l:{self.left_color} r:{self.right_color} t:{self.top_color} bo:{self.bottom_color}>'