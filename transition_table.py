#!/usr/bin/python3

class InvalidSymbol(Exception):
    def __init__(self, symbol):
        self.symb = symbol

    def symbol(self):
        return self.symb

class TransitionTable:
    def __init__(self):
        self.transitions = {
            'M' : None,
            'D' : {
                'C' : { 'C' : {'C' : None}}},
            'C' : {
                'D' : None,
                'M' : None,
                'C' : { 'C' : None}},
            'L' : {
                'X' : {'X' : {'X' : None}}},
            'X' : {
                'X' : {'X' : None},
                'L' : None,
                'C' : None},
            'V' : {
                'I' : {'I' : {'I' : None}}},
            'I' : {
                'X' : None,
                'V' : None,
                'I' : {'I' : None}
            }
        }

        self.cur_token = ''
        self.cur_pos = self.transitions

    def current_pos(self):
        return self.cur_pos

    def current_token(self):
        return self.cur_token
        
    def reset(self, symbol=None):
        if symbol not in self.transitions:
            raise InvalidSymbol(symbol)
        
        if symbol is None:
            self.cur_pos = self.transitions
            self.cur_token = ''
            return

        self.cur_pos = self.transitions[symbol]
        self.cur_token = symbol
        
    def accept(self, symbol):
        if symbol not in self.transitions:
            raise InvalidSymbol(symbol)

        if self.cur_pos is None or symbol not in self.cur_pos:
            return False;

        self.cur_pos = self.cur_pos[symbol]
        self.cur_token += symbol
        
        return True
        
    
