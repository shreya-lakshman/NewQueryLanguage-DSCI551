
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASCENDING BY CATEGORIZE COMMA DESCENDING DOLLAR EQUALS EXTRACT IDENTIFIER LIKE LIMIT NUMBER RANK STRING USING WHENquery : EXTRACT select_list USING table_list when_clause categorize_by_clause like_clause\n             | EXTRACT select_list USING table_list when_clause categorize_by_clause\n             | EXTRACT select_list USING table_list when_clause like_clauseselect_list : DOLLAR\n                   | select_list COMMA DOLLAR\n                   | IDENTIFIER\n                   | select_list COMMA IDENTIFIERtable_list : IDENTIFIERwhen_clause : WHEN conditioncategorize_by_clause : CATEGORIZE BY IDENTIFIER\n                            | CATEGORIZE BY IDENTIFIER COMMA IDENTIFIERlike_clause : LIKE STRINGcondition : IDENTIFIER EQUALS IDENTIFIER\n                 | IDENTIFIER EQUALS STRING\n                 | IDENTIFIER LIKE STRING'
    
_lr_action_items = {'EXTRACT':([0,],[2,]),'$end':([1,14,15,20,22,25,30,],[0,-2,-3,-1,-12,-10,-11,]),'DOLLAR':([2,7,],[4,10,]),'IDENTIFIER':([2,6,7,13,21,23,29,],[5,9,11,19,25,26,30,]),'USING':([3,4,5,10,11,],[6,-4,-6,-5,-7,]),'COMMA':([3,4,5,10,11,25,],[7,-4,-6,-5,-7,29,]),'WHEN':([8,9,],[13,-8,]),'CATEGORIZE':([12,18,26,27,28,],[16,-9,-13,-14,-15,]),'LIKE':([12,14,18,19,25,26,27,28,30,],[17,17,-9,24,-10,-13,-14,-15,-11,]),'BY':([16,],[21,]),'STRING':([17,23,24,],[22,27,28,]),'EQUALS':([19,],[23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,],[1,]),'select_list':([2,],[3,]),'table_list':([6,],[8,]),'when_clause':([8,],[12,]),'categorize_by_clause':([12,],[14,]),'like_clause':([12,14,],[15,20,]),'condition':([13,],[18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> EXTRACT select_list USING table_list when_clause categorize_by_clause like_clause','query',7,'p_query','lexer_parser.py',76),
  ('query -> EXTRACT select_list USING table_list when_clause categorize_by_clause','query',6,'p_query','lexer_parser.py',77),
  ('query -> EXTRACT select_list USING table_list when_clause like_clause','query',6,'p_query','lexer_parser.py',78),
  ('select_list -> DOLLAR','select_list',1,'p_select_list','lexer_parser.py',119),
  ('select_list -> select_list COMMA DOLLAR','select_list',3,'p_select_list','lexer_parser.py',120),
  ('select_list -> IDENTIFIER','select_list',1,'p_select_list','lexer_parser.py',121),
  ('select_list -> select_list COMMA IDENTIFIER','select_list',3,'p_select_list','lexer_parser.py',122),
  ('table_list -> IDENTIFIER','table_list',1,'p_table_list','lexer_parser.py',130),
  ('when_clause -> WHEN condition','when_clause',2,'p_when_clause','lexer_parser.py',134),
  ('categorize_by_clause -> CATEGORIZE BY IDENTIFIER','categorize_by_clause',3,'p_categorize_by_clause','lexer_parser.py',138),
  ('categorize_by_clause -> CATEGORIZE BY IDENTIFIER COMMA IDENTIFIER','categorize_by_clause',5,'p_categorize_by_clause','lexer_parser.py',139),
  ('like_clause -> LIKE STRING','like_clause',2,'p_like_clause','lexer_parser.py',146),
  ('condition -> IDENTIFIER EQUALS IDENTIFIER','condition',3,'p_condition','lexer_parser.py',153),
  ('condition -> IDENTIFIER EQUALS STRING','condition',3,'p_condition','lexer_parser.py',154),
  ('condition -> IDENTIFIER LIKE STRING','condition',3,'p_condition','lexer_parser.py',155),
]
