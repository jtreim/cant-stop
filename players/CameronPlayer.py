from .player import Player

class CameronPlayer(Player):
    def __init__(self, name):
        #self.pre_logic = 'I wanna be special, so here\'s an attribute I assign beforehand'
        self.single_roll_prob = {'2' : 0.132,'3' : 0.233,'4' : 0.356,'5' : 0.448,'6' : 0.561,'7' : 0.644,'8' : 0.561,'9' : 0.448,'10' : 0.356,'11' : 0.233,'12' : 0.132}
        self.prob_dict = { '6,7,8,' : 0.92,'6,7,9,' : 0.914,'5,7,8,' : 0.914,'6,8,10,' : 0.911,'4,6,8,' : 0.911,'6,7,10,' : 0.903,'4,7,8,' : 0.903,'6,8,9,' : 0.895,'5,6,8,' : 0.895,'6,7,11,' : 0.893,'5,7,10,' : 0.893,'4,7,9,' : 0.893,'3,7,8,' : 0.893,'6,7,12,' : 0.89,'2,7,8,' : 0.89,'7,8,9,' : 0.887,'5,6,7,' : 0.887,'7,8,10,' : 0.886,'4,6,7,' : 0.886,'6,8,12,' : 0.883,'4,8,10,' : 0.883,'4,6,10,' : 0.883,'2,6,8,' : 0.883,'4,7,10,' : 0.877,'5,8,9,' : 0.867,'5,6,9,' : 0.867,'7,8,11,' : 0.865,'3,6,7,' : 0.865,'7,8,12,' : 0.864,'5,8,10,' : 0.864,'4,6,9,' : 0.864,'2,6,7,' : 0.864,'5,6,10,' : 0.863,'4,8,9,' : 0.863,'6,8,11,' : 0.853,'5,7,9,' : 0.853,'3,6,8,' : 0.853,'7,9,10,' : 0.848,'4,5,7,' : 0.848,'6,9,10,' : 0.846,'4,5,8,' : 0.846,'5,7,11,' : 0.843,'3,7,9,' : 0.843,'5,7,12,' : 0.836,'5,6,11,' : 0.836,'4,7,11,' : 0.836,'3,8,9,' : 0.836,'3,7,10,' : 0.836,'2,7,9,' : 0.836,'5,8,12,' : 0.833,'4,7,12,' : 0.833,'4,6,11,' : 0.833,'3,8,10,' : 0.833,'2,7,10,' : 0.833,'2,6,9,' : 0.833,'6,9,12,' : 0.829,'2,5,8,' : 0.829,'5,8,11,' : 0.826,'3,6,9,' : 0.826,'5,6,12,' : 0.823,'4,9,10,' : 0.823,'4,8,11,' : 0.823,'4,5,10,' : 0.823,'3,6,10,' : 0.823,'2,8,9,' : 0.823,'6,10,12,' : 0.816,'4,6,12,' : 0.816,'2,8,10,' : 0.816,'2,4,8,' : 0.816,'4,8,12,' : 0.811,'2,6,10,' : 0.811,'7,9,12,' : 0.809,'2,5,7,' : 0.809,'6,9,11,' : 0.808,'3,5,8,' : 0.808,'7,10,12,' : 0.807,'2,4,7,' : 0.807,'5,9,10,' : 0.799,'4,5,9,' : 0.799,'8,9,10,' : 0.796,'6,10,11,' : 0.796,'4,5,6,' : 0.796,'3,4,8,' : 0.796,'7,10,11,' : 0.791,'3,4,7,' : 0.791,'7,9,11,' : 0.787,'3,5,7,' : 0.787,'2,7,12,' : 0.781,'5,10,11,' : 0.779,'4,5,11,' : 0.779,'3,9,10,' : 0.779,'3,7,12,' : 0.779,'3,4,9,' : 0.779,'2,7,11,' : 0.779,'5,9,11,' : 0.776,'3,7,11,' : 0.776,'3,5,9,' : 0.776,'8,9,11,' : 0.771,'3,5,6,' : 0.771,'8,9,12,' : 0.77,'2,5,6,' : 0.77,'5,9,12,' : 0.76,'2,5,9,' : 0.76,'8,10,12,' : 0.758,'4,9,11,' : 0.758,'3,8,11,' : 0.758,'3,6,11,' : 0.758,'3,5,10,' : 0.758,'2,4,6,' : 0.758,'6,11,12,' : 0.756,'5,10,12,' : 0.756,'4,10,11,' : 0.756,'4,9,12,' : 0.756,'3,8,12,' : 0.756,'3,4,10,' : 0.756,'2,6,11,' : 0.756,'2,5,10,' : 0.756,'2,4,9,' : 0.756,'2,3,8,' : 0.756,'7,11,12,' : 0.752,'2,3,7,' : 0.752,'8,10,11,' : 0.742,'3,4,6,' : 0.742,'4,10,12,' : 0.738,'2,8,12,' : 0.738,'2,6,12,' : 0.738,'2,4,10,' : 0.738,'3,6,12,' : 0.736,'2,8,11,' : 0.736,'5,11,12,' : 0.712,'3,9,12,' : 0.712,'2,5,11,' : 0.712,'2,3,9,' : 0.712,'4,5,12,' : 0.71,'3,9,11,' : 0.71,'3,5,11,' : 0.71,'2,9,10,' : 0.71,'8,11,12,' : 0.684,'2,3,6,' : 0.684,'9,10,11,' : 0.669,'3,4,5,' : 0.669,'9,10,12,' : 0.657,'3,10,11,' : 0.657,'3,4,11,' : 0.657,'2,4,5,' : 0.657,'3,5,12,' : 0.637,'2,9,11,' : 0.637,'4,11,12,' : 0.634,'3,10,12,' : 0.634,'2,9,12,' : 0.634,'2,5,12,' : 0.634,'2,4,11,' : 0.634,'2,3,10,' : 0.634,'9,11,12,' : 0.584,'2,3,5,' : 0.584,'3,4,12,' : 0.579,'2,10,11,' : 0.579,'2,10,12,' : 0.552,'2,4,12,' : 0.552,'3,11,12,' : 0.525,'2,3,11,' : 0.525,'10,11,12,' : 0.522,'2,3,4,' : 0.522,'2,11,12,' : 0.438,'2,3,12,' : 0.438,'2,3,4,' : 0.522,'2,3,5,' : 0.584,'2,3,6,' : 0.684,'2,3,7,' : 0.752,'2,3,8,' : 0.756,'2,3,9,' : 0.712,'2,3,10,' : 0.634,'2,3,11,' : 0.525,'2,3,12,' : 0.438,'2,4,5,' : 0.657,'2,4,6,' : 0.758,'2,4,7,' : 0.807,'2,4,8,' : 0.816,'2,4,9,' : 0.756,'2,4,10,' : 0.738,'2,4,11,' : 0.634,'2,4,12,' : 0.552,'2,5,6,' : 0.77,'2,5,7,' : 0.809,'2,5,8,' : 0.829,'2,5,9,' : 0.76,'2,5,10,' : 0.756,'2,5,11,' : 0.712,'2,5,12,' : 0.634,'2,6,7,' : 0.864,'2,6,8,' : 0.883,'2,6,9,' : 0.833,'2,6,10,' : 0.811,'2,6,11,' : 0.756,'2,6,12,' : 0.738,'2,7,8,' : 0.89,'2,7,9,' : 0.836,'2,7,10,' : 0.833,'2,7,11,' : 0.779,'2,7,12,' : 0.781,'2,8,9,' : 0.823,'2,8,10,' : 0.816,'2,8,11,' : 0.736,'2,8,12,' : 0.738,'2,9,10,' : 0.71,'2,9,11,' : 0.637,'2,9,12,' : 0.634,'2,10,11,' : 0.579,'2,10,12,' : 0.552,'2,11,12,' : 0.438,'3,4,5,' : 0.669,'3,4,6,' : 0.742,'3,4,7,' : 0.791,'3,4,8,' : 0.796,'3,4,9,' : 0.779,'3,4,10,' : 0.756,'3,4,11,' : 0.657,'3,4,12,' : 0.579,'3,5,6,' : 0.771,'3,5,7,' : 0.787,'3,5,8,' : 0.808,'3,5,9,' : 0.776,'3,5,10,' : 0.758,'3,5,11,' : 0.71,'3,5,12,' : 0.637,'3,6,7,' : 0.865,'3,6,8,' : 0.853,'3,6,9,' : 0.826,'3,6,10,' : 0.823,'3,6,11,' : 0.758,'3,6,12,' : 0.736,'3,7,8,' : 0.893,'3,7,9,' : 0.843,'3,7,10,' : 0.836,'3,7,11,' : 0.776,'3,7,12,' : 0.779,'3,8,9,' : 0.836,'3,8,10,' : 0.833,'3,8,11,' : 0.758,'3,8,12,' : 0.756,'3,9,10,' : 0.779,'3,9,11,' : 0.71,'3,9,12,' : 0.712,'3,10,11,' : 0.657,'3,10,12,' : 0.634,'3,11,12,' : 0.525,'4,5,6,' : 0.796,'4,5,7,' : 0.848,'4,5,8,' : 0.846,'4,5,9,' : 0.799,'4,5,10,' : 0.823,'4,5,11,' : 0.779,'4,5,12,' : 0.71,'4,6,7,' : 0.886,'4,6,8,' : 0.911,'4,6,9,' : 0.864,'4,6,10,' : 0.883,'4,6,11,' : 0.833,'4,6,12,' : 0.816,'4,7,8,' : 0.903,'4,7,9,' : 0.893,'4,7,10,' : 0.877,'4,7,11,' : 0.836,'4,7,12,' : 0.833,'4,8,9,' : 0.863,'4,8,10,' : 0.883,'4,8,11,' : 0.823,'4,8,12,' : 0.811,'4,9,10,' : 0.823,'4,9,11,' : 0.758,'4,9,12,' : 0.756,'4,10,11,' : 0.756,'4,10,12,' : 0.738,'4,11,12,' : 0.634,'5,6,7,' : 0.887,'5,6,8,' : 0.895,'5,6,9,' : 0.867,'5,6,10,' : 0.863,'5,6,11,' : 0.836,'5,6,12,' : 0.823,'5,7,8,' : 0.914,'5,7,9,' : 0.853,'5,7,10,' : 0.893,'5,7,11,' : 0.843,'5,7,12,' : 0.836,'5,8,9,' : 0.867,'5,8,10,' : 0.864,'5,8,11,' : 0.826,'5,8,12,' : 0.833,'5,9,10,' : 0.799,'5,9,11,' : 0.776,'5,9,12,' : 0.76,'5,10,11,' : 0.779,'5,10,12,' : 0.756,'5,11,12,' : 0.712,'6,7,8,' : 0.92,'6,7,9,' : 0.914,'6,7,10,' : 0.903,'6,7,11,' : 0.893,'6,7,12,' : 0.89,'6,8,9,' : 0.895,'6,8,10,' : 0.911,'6,8,11,' : 0.853,'6,8,12,' : 0.883,'6,9,10,' : 0.846,'6,9,11,' : 0.808,'6,9,12,' : 0.829,'6,10,11,' : 0.796,'6,10,12,' : 0.816,'6,11,12,' : 0.756,'7,8,9,' : 0.887,'7,8,10,' : 0.886,'7,8,11,' : 0.865,'7,8,12,' : 0.864,'7,9,10,' : 0.848,'7,9,11,' : 0.787,'7,9,12,' : 0.809,'7,10,11,' : 0.791,'7,10,12,' : 0.807,'7,11,12,' : 0.752,'8,9,10,' : 0.796,'8,9,11,' : 0.771,'8,9,12,' : 0.77,'8,10,11,' : 0.742,'8,10,12,' : 0.758,'8,11,12,' : 0.684,'9,10,11,' : 0.669,'9,10,12,' : 0.657,'9,11,12,' : 0.584,'10,11,12,' : 0.522}
        self.original_board = {}
        self.completed_aisles = {}
        self.org_my_completed_aisles = {}
        self.my_completed_aisles = {}
        self.my_steps_away = {}
        self.opponent_comp = {}
        self.opponent_max_per = {}
        self.opponent_max = []
        self.how_close_opp = {}
        self.num_sel_count = 0
        self.num_sel = [] 
        self.num_sel_str = ""
        self.closeness_w = .48
        self.prob_w = .32
        self.opp_lead_w = .2
        self.single_r_threshold = .02
        self.full_r_threshold = .47
        self.opp_close_always_roll_threshold = 2.67
        super(CameronPlayer, self).__init__(name)
        #self.post_logic = 'I wanna be extra special, so here\'s another attribute I assign later'

  
    def is_continuing_turn(self, board, changes):
        
        self.set_stage(board,changes)
        self.my_progress(board, changes)
        self.closest_opp(board)
        
        #Stop if I finish my third aisle 
        if sum(x == 1 for x in self.my_completed_aisles.values()) == 3:
            return False
        
        #Continue if an oppenent has 2 rows finished and is more than 66% finished with a third always keep rolling
        elif max(self.how_close_opp.values())> self.opp_close_always_roll_threshold:
            return True
        
        #Stop if I finish at least 1 aisle
        elif sum(x == 1 for x in self.my_completed_aisles.values()) > sum(x == 1 for x in self.org_my_completed_aisles.values()):
            return False
        
        #Continue if I don't have 3 numbers and haven't rolled a unlikely single roll comb        
        elif self.num_sel_count < 3 and self.single_roll(changes) > self.single_r_threshold:
            return True
        
        #Stop if getting to where I have gotten would be a less than 50% chance
        elif self.single_roll(changes) <= self.single_r_threshold or self.full_roll(changes) <  self.full_r_threshold:
            #print(self.single_roll(changes))
            #print(self.full_roll(changes))
            return False
        else:
            return True
 
    
    
    def set_stage(self, board, changes):

        if changes['turn'] == 0:
            self.original_board = board.copy()
            
        self.num_sel_count = 0 
        self.num_sel = []
        self.num_sel_str = ""
    
        for num_key, progress in changes.items():
            if progress > 0 and num_key != 'turn':
                self.num_sel.append(num_key)
                self.num_sel_count += 1
                self.num_sel_str = self.num_sel_str + num_key + ","
                 
    def single_roll(self,chng):
        if self.num_sel_count == 0:
            return 1
        a_prob_list = []
        for n in self.num_sel:
            a_prob_list.append(self.single_roll_prob[n]**(chng[n]))
        return min(a_prob_list)
            
    def full_roll(self,chng):
        if self.num_sel_count != 3:
            return 1
        else:
            try:
                return self.prob_dict[self.num_sel_str]**(chng['turn']-1)
            except:
                return 1
            
    def completed(self,brd):
        for key in brd.keys():
            temp_list = []
            for tupp in brd[key]['players']:
                temp_list.append(tupp[1]/brd[key]['steps'])
                self.completed_aisles[key] = max(temp_list)
    
    def my_progress(self,brd,chng):
        for key in brd.keys():
            for tupp in brd[key]['players']:
                if tupp[0] == 'Cameron':
                    self.org_my_completed_aisles[key] = (tupp[1])/brd[key]['steps']
                    self.my_completed_aisles[key] = (tupp[1]+chng[key])/brd[key]['steps']
                    self.my_steps_away[key] = brd[key]['steps'] - (tupp[1]+chng[key])
    
    
    def closest_opp(self,brd):
        self.opponent_comp.clear()
        self.opponent_max_per.clear()
        self.opponent_max.clear()
        
        
        #opponent_comp and opponent_max_per dict
        for key in brd.keys():
            for tupp in brd[key]['players']:
                if tupp[0] != 'Cameron':
                    if not tupp[0] in self.opponent_comp:
                           self.opponent_comp[tupp[0]]= 0
                    if (tupp[1]/brd[key]['steps'])==1:
                       self.opponent_comp[tupp[0]]+= 1
                    
                    if not tupp[0] in self.opponent_max_per:
                        self.opponent_max_per[tupp[0]] = []
                    self.opponent_max_per[tupp[0]].append((tupp[1]/brd[key]['steps']))
                    
        for tupp in brd['2']['players']:
            if tupp[0] != 'Cameron':
                if not tupp[0] in self.how_close_opp:
                    self.how_close_opp[tupp[0]] = 0
                self.how_close_opp[tupp[0]] = self.opponent_comp[tupp[0]]+max([x for x in self.opponent_max_per[tupp[0]] if x != 1]) 
        
        
        for i in range(11):
            a_list = []
            for opp in self.opponent_max_per:
                a_list.append(self.opponent_max_per[opp][i])
            self.opponent_max.append(max(a_list))
            
            
    def score_move(self, mv,brd,chng):
        

            
        if len(mv) == 1:
            die_string = str(mv[0])
            finish_flag = 0
            if self.my_steps_away[die_string] == 1:
                finish_flag = 10
                
            if self.num_sel_count == 3:
                single_roll_prob = 1-self.single_roll_prob[die_string]
            else:
                single_roll_prob = self.single_roll_prob[die_string]            
                
            opp_less_me = abs(self.opponent_max[int(die_string)-2] - self.my_completed_aisles[die_string])
            
            score = (single_roll_prob*self.prob_w) + (self.my_completed_aisles[die_string]*self.closeness_w) + ((1-opp_less_me)*self.opp_lead_w) + finish_flag
        
        elif len(mv) == 2:
            die_1 = str(mv[0])
            die_2 = str(mv[1])
            finish_flag_1 = 0
            finish_flag_2 = 0
            
            if self.my_steps_away[die_1] == 1:
                finish_flag_1 = 10
            if self.my_steps_away[die_2] == 1:
                finish_flag_2 = 10
                
                
            opp_less_me_1 = abs(self.opponent_max[int(die_1)-2] - self.my_completed_aisles[die_1])
            opp_less_me_2 = abs(self.opponent_max[int(die_2)-2] - self.my_completed_aisles[die_2])
            
            
            if self.num_sel_count == 3:
                single_roll_prob_1 = 1-self.single_roll_prob[die_1]
                single_roll_prob_2 = 1-self.single_roll_prob[die_2]
            else:
                single_roll_prob_1 = self.single_roll_prob[die_1] 
                single_roll_prob_2 = self.single_roll_prob[die_2] 

            
            score_1 = (single_roll_prob_1*self.prob_w) + (self.my_completed_aisles[die_1]*self.closeness_w) + ((1-opp_less_me_1)*self.opp_lead_w) + finish_flag_1
            score_2 = (single_roll_prob_2*self.prob_w) + (self.my_completed_aisles[die_2]*self.closeness_w) + ((1-opp_less_me_2)*self.opp_lead_w) + finish_flag_2
            
            repeat_double = 0
            if die_1 == die_2:
                repeat_double = 5
            
            
            if self.num_sel_count == 0:
                two_num_pri_ratio = .6
            elif self.num_sel_count == 1:
                two_num_pri_ratio = .7
            elif self.num_sel_count == 2:
                two_num_pri_ratio = .8
            elif self.num_sel_count == 3:
                two_num_pri_ratio = 1    
            else:
                two_num_pri_ratio = .5    
                
                
                
                
            score = (score_1 + score_2)*two_num_pri_ratio + repeat_double
        
        else:
            score = .5
        
        
        return score
            
    
 
    
    def choose_move(self, moves, board, changes, invalid_move=False):

        self.set_stage(board,changes)
        self.my_progress(board, changes)
        self.closest_opp(board)
        self.completed(board)
            
        score_list = []
        for move in moves:
            score_list.append(self.score_move(move,board,changes))
        #print(score_list)
        
        try:
            return moves[score_list.index(max(score_list))]
        except:
            return moves[0]
                
