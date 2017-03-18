from __future__ import division, print_function
from retic.runtime import *
from retic.mgd_transient import *
from retic.typing import *

def check13(val, elim, act):
    try:
        val.links
        val.id
        val.pos
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def check16(val, elim, act):
    try:
        val.nodes_by_id
        val.count
        val.get_by_id
        val.size
        val.contains_pos
        val.link_nodes
        val.get_by_pos
        val.nodes_by_pos
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def check0(val, elim, act):
    try:
        val.x
        val.y
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def check1(val, elim, act):
    try:
        val.next_cell_highest_value
        val.count
        val.already_done
        val.filter_tiles
        val.next_cell
        val.HIGHEST_VALUE_STRATEGY
        val.next_cell_max_choice
        val.next_cell_min_choice
        val.set_done
        val.__getitem__
        val.MIN_CHOICE_STRATEGY
        val.remove
        val.clone
        val.remove_all
        val.remove_unfixed
        val.next_cell_max_neighbors
        val.next_cell_min_neighbors
        val.cells
        val.next_cell_first
        val.MAX_CHOICE_STRATEGY
        val.FIRST_STRATEGY
        val.MAX_NEIGHBORS_STRATEGY
        val.MIN_NEIGHBORS_STRATEGY
        add_blame_pointer(val, elim, act)
        return val
    except:
        blame(val, elim, act)

def cast30(val, src, b, trg):
    try:
        val.splitlines
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast19(val, src, b, trg):
    try:
        val.clone
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast10(val, src, b, trg):
    try:
        val.next_cell_max_neighbors
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast11(val, src, b, trg):
    try:
        val.next_cell_min_neighbors
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast4(val, src, b, trg):
    try:
        val.get_by_id
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast26(val, src, b, trg):
    try:
        val.append
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast35(val, src, b, trg):
    try:
        val.parse_args
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast20(val, src, b, trg):
    try:
        val.already_done
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast31(val, src, b, trg):
    try:
        val.strip
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast8(val, src, b, trg):
    try:
        val.next_cell_max_choice
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast34(val, src, b, trg):
    try:
        val.OptionParser
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast18(val, src, b, trg):
    try:
        val.done
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast14(val, src, b, trg):
    try:
        val.nodes_by_pos
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast28(val, src, b, trg):
    try:
        val.get_by_pos
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast33(val, src, b, trg):
    try:
        val.getvalue
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast12(val, src, b, trg):
    try:
        val.count
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast32(val, src, b, trg):
    try:
        val.nodes_by_id
        val.count
        val.get_by_id
        val.size
        val.contains_pos
        val.link_nodes
        val.get_by_pos
        val.nodes_by_pos
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast24(val, src, b, trg):
    try:
        val.set_done
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast6(val, src, b, trg):
    try:
        val.next_cell_highest_value
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast25(val, src, b, trg):
    try:
        val.next_cell
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast15(val, src, b, trg):
    try:
        val.nodes_by_id
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast3(val, src, b, trg):
    try:
        val.hex
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast27(val, src, b, trg):
    try:
        val.size
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast29(val, src, b, trg):
    try:
        val.id
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast2(val, src, b, trg):
    try:
        val.next_cell_highest_value
        val.count
        val.next_cell
        val.filter_tiles
        val.already_done
        val.HIGHEST_VALUE_STRATEGY
        val.next_cell_max_choice
        val.next_cell_min_choice
        val.set_done
        val.__getitem__
        val.MIN_CHOICE_STRATEGY
        val.remove
        val.clone
        val.remove_all
        val.remove_unfixed
        val.next_cell_max_neighbors
        val.next_cell_min_neighbors
        val.cells
        val.next_cell_first
        val.MAX_CHOICE_STRATEGY
        val.FIRST_STRATEGY
        val.MAX_NEIGHBORS_STRATEGY
        val.MIN_NEIGHBORS_STRATEGY
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast23(val, src, b, trg):
    try:
        val.remove_unfixed
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast22(val, src, b, trg):
    try:
        val.cells
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast5(val, src, b, trg):
    try:
        val.links
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast17(val, src, b, trg):
    try:
        val.tiles
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast9(val, src, b, trg):
    try:
        val.next_cell_first
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast7(val, src, b, trg):
    try:
        val.next_cell_min_choice
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])

def cast21(val, src, b, trg):
    try:
        val.remove
        add_blame_cast(val, src, b, trg)
        return val
    except:
        do_blame([b])
gensym1025 = Dyn
gensym1325 = Tuple(Dyn, Dyn)
gensym775 = Dyn
gensym823 = Dyn
gensym972 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym1116 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1170 = Dyn
gensym355 = Object('', {'links': Dyn, })
gensym645 = Dyn
gensym38 = Dyn
gensym89 = List(List(Int))
gensym318 = Dyn
gensym1049 = Dyn
gensym707 = Object('', {'remove': Dyn, })
gensym1036 = Function(AnonymousParameters([Dyn]), Dyn)
gensym929 = String
gensym1148 = Dyn
gensym26 = Int
gensym1077 = Dyn
gensym172 = Int
gensym941 = String
gensym21 = Dyn
gensym1137 = Object('', {'done': Dyn, })
gensym305 = Dyn
gensym103 = Function(AnonymousParameters([Int]), Dyn)
gensym739 = Dyn
gensym1411 = Object('', {'parse_args': Dyn, })
gensym1237 = Dyn
gensym708 = Dyn
gensym398 = Object('', {'next_cell_min_neighbors': Dyn, })
gensym792 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym1110 = Function(AnonymousParameters([]), Dyn)
gensym1264 = Function(AnonymousParameters([Dyn]), Dyn)
gensym280 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1404 = List(Dyn)
gensym1122 = Function(AnonymousParameters([]), Dyn)
gensym798 = Bool
gensym1112 = Int
gensym987 = Dyn
gensym653 = Dyn
gensym592 = Object('', {'cells': Dyn, })
gensym1244 = Object('', {'splitlines': Dyn, })
gensym391 = Dyn
gensym386 = Object('', {'next_cell_first': Dyn, })
gensym779 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym192 = Int
gensym714 = Dyn
gensym1232 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym851 = Dyn
gensym879 = Dyn
gensym864 = Function(AnonymousParameters([Dyn]), Dyn)
gensym251 = Function(AnonymousParameters([Int]), Dyn)
gensym873 = Dyn
gensym529 = Dyn
gensym56 = Dyn
gensym765 = Dyn
gensym858 = Object('', {'hex': Dyn, })
gensym362 = Int
gensym833 = Dyn
gensym512 = Function(NamedParameters([('self', Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), }))]), Dyn)
gensym1213 = Dyn
gensym735 = Dyn
gensym471 = Dict(Dyn, Dyn)
gensym384 = Int
gensym1394 = Function(AnonymousParameters([]), Dyn)
gensym361 = Dyn
gensym632 = Object('', {'get_by_id': Dyn, })
gensym150 = Function(AnonymousParameters([Int]), Dyn)
gensym1375 = Dyn
gensym1061 = Int
gensym1172 = Dyn
gensym450 = Object('', {'nodes_by_pos': Dyn, })
gensym232 = Function(AnonymousParameters([Int]), Dyn)
gensym226 = Function(AnonymousParameters([Dyn]), Dyn)
gensym457 = Tuple(Dyn, Dyn)
gensym666 = Dyn
gensym85 = Function(AnonymousParameters([Int]), Dyn)
gensym153 = Dyn
gensym993 = String
gensym877 = String
gensym1072 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1415 = Tuple(Dyn, Dyn)
gensym902 = Function(AnonymousParameters([Dyn]), Dyn)
gensym545 = Dyn
gensym656 = Function(AnonymousParameters([Dyn]), Dyn)
gensym613 = Dyn
gensym556 = Function(AnonymousParameters([Dyn, Dyn, Dyn]), Dyn)
gensym1241 = Dyn
gensym1101 = Dyn
gensym837 = Dyn
gensym567 = Dyn
gensym1008 = Object('', {'hex': Dyn, })
gensym1071 = Dyn
gensym626 = Function(AnonymousParameters([Dyn]), Dyn)
gensym234 = Int
gensym503 = Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })
gensym396 = Int
gensym1358 = Function(AnonymousParameters([Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Dyn), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), }), List(Int), Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'next_cell': Function(DynParameters, Int), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'already_done': Function(NamedParameters([('i', Int)]), Dyn), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Dyn), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })]), Dyn)
gensym1278 = Function(AnonymousParameters([Dyn]), Dyn)
gensym109 = Function(AnonymousParameters([Int]), Dyn)
gensym133 = Bool
gensym110 = Dyn
gensym688 = Dyn
gensym651 = Dyn
gensym453 = Dyn
gensym321 = Object('', {'links': Dyn, })
gensym258 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('pos', Dyn)]), Int)
gensym156 = Function(AnonymousParameters([Int]), Dyn)
gensym1125 = Int
gensym227 = Int
gensym906 = Object('', {'get_by_pos': Dyn, })
gensym1154 = Int
gensym8 = Int
gensym602 = Object('', {'count': Dyn, })
gensym852 = Object('', {'set_done': Dyn, })
gensym300 = Function(AnonymousParameters([Dyn]), Dyn)
gensym420 = Dyn
gensym579 = Dyn
gensym957 = Dyn
gensym1352 = Tuple(Int, Int)
gensym1146 = Dyn
gensym674 = Function(AnonymousParameters([Dyn]), Dyn)
gensym108 = Dyn
gensym468 = Dyn
gensym412 = Function(NamedParameters([('self', Dyn), ('size', Int)]), Dyn)
gensym1068 = Object('', {'links': Dyn, })
gensym961 = String
gensym183 = Int
gensym485 = Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })
gensym504 = Dyn
gensym540 = Object('', {'count': Dyn, })
gensym883 = Dyn
gensym771 = Dyn
gensym838 = List(Tuple(Dyn, Dyn))
gensym892 = Dyn
gensym62 = Dyn
gensym538 = Dyn
gensym430 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym1246 = Function(AnonymousParameters([]), Dyn)
gensym71 = Dyn
gensym129 = Bool
gensym694 = Object('', {'get_by_id': Dyn, })
gensym1388 = Function(AnonymousParameters([]), Dyn)
gensym1295 = Dyn
gensym926 = Object('', {'id': Dyn, })
gensym608 = Object('', {'get_by_id': Dyn, })
gensym1217 = Int
gensym633 = Dyn
gensym1277 = Dyn
gensym117 = Dyn
gensym727 = Bool
gensym233 = Dyn
gensym588 = Object('', {'cells': Dyn, })
gensym585 = Dyn
gensym385 = Dyn
gensym1197 = Dyn
gensym1274 = Int
gensym916 = Dyn
gensym221 = Dyn
gensym709 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym489 = Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })
gensym671 = Dyn
gensym705 = Function(AnonymousParameters([Int]), Dyn)
gensym1392 = Function(AnonymousParameters([Dyn]), Dyn)
gensym171 = Dyn
gensym238 = Dyn
gensym195 = Dyn
gensym1013 = Dyn
gensym1417 = Dyn
gensym552 = Object('', {'clone': Dyn, })
gensym97 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('i', Int)]), Bool)
gensym275 = Dyn
gensym1027 = Dyn
gensym207 = Dyn
gensym476 = Function(AnonymousParameters([Int]), Dyn)
gensym910 = Object('', {'id': Dyn, })
gensym139 = Function(AnonymousParameters([Int]), Dyn)
gensym1179 = Dyn
gensym390 = Int
gensym1201 = Dyn
gensym524 = Tuple(Int, Int)
gensym1331 = Dyn
gensym813 = Dyn
gensym473 = Int
gensym1326 = Tuple(Int, Int)
gensym847 = Dyn
gensym936 = Object('', {'done': Dyn, })
gensym1164 = Object('', {'count': Dyn, })
gensym154 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym684 = Object('', {'already_done': Dyn, })
gensym247 = Function(AnonymousParameters([Int]), Dyn)
gensym122 = Dyn
gensym142 = Dyn
gensym454 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym1046 = Dyn
gensym637 = Dyn
gensym4 = Int
gensym965 = Dyn
gensym174 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym67 = List(List(Int))
gensym194 = Int
gensym1052 = Function(AnonymousParameters([Dyn]), Dyn)
gensym591 = Dyn
gensym664 = Object('', {'links': Dyn, })
gensym625 = Dyn
gensym1191 = Dyn
gensym1180 = Object('', {'strip': Dyn, })
gensym682 = Object('', {'links': Dyn, })
gensym995 = String
gensym1384 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym506 = Object('', {'nodes_by_id': Dyn, })
gensym1051 = Dyn
gensym750 = Dyn
gensym1192 = Function(AnonymousParameters([Dyn]), Dyn)
gensym20 = Int
gensym34 = Dyn
gensym0 = Dyn
gensym1318 = Int
gensym922 = Object('', {'get_by_pos': Dyn, })
gensym152 = Int
gensym1410 = Dyn
gensym134 = Dyn
gensym173 = Dyn
gensym1418 = Function(NamedParameters([('n', Dyn), ('timer', Dyn)]), Dyn)
gensym325 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1381 = Dyn
gensym611 = Dyn
gensym917 = Dyn
gensym128 = Int
gensym1082 = Dyn
gensym557 = Dyn
gensym249 = Function(AnonymousParameters([Int]), Dyn)
gensym1395 = Dyn
gensym302 = Object('', {'links': Dyn, })
gensym1042 = Object('', {'tiles': Dyn, })
gensym440 = Object('', {'count': Dyn, })
gensym820 = List(Tuple(Dyn, Dyn))
gensym439 = Dyn
gensym448 = Dyn
gensym335 = Object('', {'links': Dyn, })
gensym997 = Dyn
gensym511 = Dyn
gensym79 = Dyn
gensym774 = Object('', {'already_done': Dyn, })
gensym274 = Function(AnonymousParameters([Int]), Dyn)
gensym24 = Int
gensym606 = Object('', {'hex': Dyn, })
gensym532 = Function(NamedParameters([('self', Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), })), ('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, }))
gensym861 = Dyn
gensym1351 = Tuple(Dyn, Dyn)
gensym834 = List(Tuple(Dyn, Dyn))
gensym598 = Function(AnonymousParameters([Dyn]), Dyn)
gensym102 = Dyn
gensym13 = Dyn
gensym371 = Dyn
gensym804 = Object('', {'next_cell': Dyn, })
gensym52 = Dyn
gensym272 = Function(AnonymousParameters([Dyn]), Dyn)
gensym397 = Dyn
gensym1012 = Object('', {'done': Dyn, })
gensym1088 = Int
gensym424 = Object('', {'nodes_by_id': Dyn, })
gensym1315 = Dyn
gensym698 = Object('', {'links': Dyn, })
gensym928 = Function(AnonymousParameters([Dyn]), Dyn)
gensym204 = Dyn
gensym268 = Object('', {'links': Dyn, })
gensym717 = Function(AnonymousParameters([Dyn]), Dyn)
gensym392 = Object('', {'next_cell_max_neighbors': Dyn, })
gensym271 = Dyn
gensym1103 = Dyn
gensym1058 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1083 = Dyn
gensym1362 = Function(NamedParameters([]), Dyn)
gensym658 = Object('', {'hex': Dyn, })
gensym1168 = Function(NamedParameters([('pos', Dyn), ('strategy', Int), ('order', Int), ('output', Dyn)]), Int)
gensym983 = Dyn
gensym80 = Bool
gensym419 = List(Dyn)
gensym1173 = Dyn
gensym863 = Dyn
gensym1368 = Function(AnonymousParameters([]), Dyn)
gensym1210 = Function(AnonymousParameters([String]), Dyn)
gensym261 = Dyn
gensym1035 = Dyn
gensym1321 = Tuple(Dyn, Dyn)
gensym981 = Dyn
gensym311 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('pos', Dyn)]), Int)
gensym962 = Dyn
gensym584 = Object('', {'links': Dyn, })
gensym270 = Int
gensym53 = Function(AnonymousParameters([Int]), Dyn)
gensym7 = Dyn
gensym667 = Dyn
gensym1117 = Int
gensym1202 = Function(AnonymousParameters([Dyn]), Dyn)
gensym660 = Object('', {'get_by_id': Dyn, })
gensym803 = Dyn
gensym415 = Dyn
gensym1070 = Object('', {'already_done': Dyn, })
gensym839 = Dyn
gensym589 = Dyn
gensym1119 = Dyn
gensym387 = Dyn
gensym1337 = Dyn
gensym380 = Object('', {'next_cell_max_choice': Dyn, })
gensym291 = Dyn
gensym1409 = Function(DynParameters, Dyn)
gensym1263 = Dyn
gensym1085 = Dyn
gensym138 = Dyn
gensym680 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1377 = Dyn
gensym900 = Object('', {'size': Dyn, })
gensym1323 = Dyn
gensym1091 = Dyn
gensym1133 = Object('', {'hex': Dyn, })
gensym1389 = Dyn
gensym1023 = Dyn
gensym1156 = Dyn
gensym690 = Dyn
gensym923 = Dyn
gensym277 = Dyn
gensym95 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('i', Int), ('v', Int)]), Dyn)
gensym576 = Object('', {'links': Dyn, })
gensym436 = Object('', {'nodes_by_id': Dyn, })
gensym231 = Dyn
gensym84 = Dyn
gensym1065 = Dyn
gensym1169 = Int
gensym292 = Function(AnonymousParameters([Int]), Dyn)
gensym768 = Object('', {'get_by_id': Dyn, })
gensym548 = Object('', {'tiles': Dyn, })
gensym1020 = Function(AnonymousParameters([Dyn]), Dyn)
gensym287 = Int
gensym1030 = Object('', {'count': Dyn, })
gensym1374 = Object('', {'getvalue': Dyn, })
gensym575 = Dyn
gensym1019 = Dyn
gensym1407 = Object('', {'OptionParser': Dyn, })
gensym683 = Dyn
gensym1134 = Dyn
gensym670 = Object('', {'done': Dyn, })
gensym1135 = Object('', {'tiles': Dyn, })
gensym938 = Object('', {'size': Dyn, })
gensym1190 = Object('', {'count': Dyn, })
gensym1336 = Dyn
gensym381 = Dyn
gensym144 = Dyn
gensym623 = Dyn
gensym1296 = Int
gensym843 = Dyn
gensym135 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('tiles', List(Int))]), Dyn)
gensym1174 = Function(NamedParameters([('file', Dyn)]), Dyn)
gensym930 = Dyn
gensym219 = Dyn
gensym805 = Dyn
gensym93 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('i', Int)]), List(Int))
gensym553 = Dyn
gensym986 = Object('', {'already_done': Dyn, })
gensym214 = Int
gensym1320 = Int
gensym127 = Dyn
gensym1006 = Dyn
gensym542 = Object('', {'count': Dyn, })
gensym522 = Tuple(Int, Int)
gensym257 = Dyn
gensym1294 = Function(AnonymousParameters([Dyn]), Dyn)
gensym100 = Dyn
gensym618 = Object('', {'count': Dyn, })
gensym1268 = Int
gensym228 = Dyn
gensym1105 = Dyn
gensym1260 = Function(AnonymousParameters([Dyn]), Dyn)
gensym306 = Function(AnonymousParameters([Dyn]), Dyn)
gensym185 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym288 = Dyn
gensym168 = Int
gensym517 = Dyn
gensym351 = Object('', {'get_by_id': Dyn, })
gensym475 = Dyn
gensym657 = Dyn
gensym125 = Dyn
gensym253 = Int
gensym908 = Function(AnonymousParameters([Tuple(Dyn, Dyn)]), Dyn)
gensym829 = Dyn
gensym918 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym1132 = Dyn
gensym980 = Object('', {'get_by_pos': Dyn, })
gensym624 = Object('', {'get_by_id': Dyn, })
gensym31 = Dyn
gensym437 = Dyn
gensym1037 = Dyn
gensym427 = Dyn
gensym655 = Dyn
gensym921 = Dyn
gensym1349 = Dyn
gensym1247 = Dyn
gensym867 = Dyn
gensym1347 = Tuple(Dyn, Dyn)
gensym893 = String
gensym1261 = Dyn
gensym304 = Int
gensym495 = Dyn
gensym1271 = Dyn
gensym940 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1029 = Dyn
gensym514 = Object('', {'pos': Dyn, })
gensym700 = Object('', {'already_done': Dyn, })
gensym780 = Dyn
gensym1214 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1048 = Dyn
gensym898 = Object('', {'done': Dyn, })
gensym180 = Dyn
gensym1147 = Function(AnonymousParameters([Int]), Dyn)
gensym353 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1176 = Object('', {'splitlines': Dyn, })
gensym49 = Dyn
gensym543 = Dyn
gensym328 = Dyn
gensym1308 = Int
gensym1100 = Int
gensym345 = Function(AnonymousParameters([Int]), Dyn)
gensym761 = Int
gensym600 = Object('', {'cells': Dyn, })
gensym905 = Dyn
gensym695 = Dyn
gensym1080 = Function(DynParameters, Int)
gensym239 = Dyn
gensym1343 = Dyn
gensym422 = Object('', {'nodes_by_pos': Dyn, })
gensym17 = Dyn
gensym451 = Dyn
gensym359 = Function(AnonymousParameters([Dyn]), Dyn)
gensym810 = Function(AnonymousParameters([List(Tuple(Dyn, Dyn))]), Dyn)
gensym435 = Dyn
gensym303 = Dyn
gensym452 = Object('', {'nodes_by_id': Dyn, })
gensym1200 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym919 = Dyn
gensym794 = Dyn
gensym942 = Dyn
gensym850 = Object('', {'done': Dyn, })
gensym115 = Dyn
gensym411 = Dyn
gensym914 = Dyn
gensym260 = Function(AnonymousParameters([Int]), Dyn)
gensym428 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym711 = Dyn
gensym874 = Function(AnonymousParameters([Dyn]), Dyn)
gensym87 = Int
gensym704 = Dyn
gensym1285 = Dyn
gensym604 = Function(AnonymousParameters([Dyn]), Dyn)
gensym720 = Function(AnonymousParameters([Int]), Dyn)
gensym636 = Object('', {'links': Dyn, })
gensym1265 = Dyn
gensym931 = String
gensym200 = Dyn
gensym1354 = Int
gensym1063 = Dyn
gensym583 = Dyn
gensym18 = Int
gensym367 = Dyn
gensym836 = Dyn
gensym939 = Dyn
gensym323 = Int
gensym572 = Object('', {'get_by_id': Dyn, })
gensym421 = Dyn
gensym69 = Dyn
gensym832 = Dyn
gensym1131 = Function(NamedParameters([('pos', Dyn)]), Dyn)
gensym347 = Int
gensym193 = Dyn
gensym1300 = Dyn
gensym953 = Dyn
gensym855 = Dyn
gensym197 = Function(AnonymousParameters([Int]), Dyn)
gensym1279 = Dyn
gensym254 = Dyn
gensym715 = Object('', {'cells': Dyn, })
gensym123 = Dyn
gensym70 = Bool
gensym297 = Dyn
gensym853 = Dyn
gensym209 = Dyn
gensym559 = Void
gensym1319 = Dyn
gensym82 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'next_cell': Function(DynParameters, Int), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym1074 = Bool
gensym338 = Dyn
gensym1242 = Int
gensym659 = Dyn
gensym870 = Function(AnonymousParameters([Dyn]), Dyn)
gensym895 = Dyn
gensym1386 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1056 = Object('', {'already_done': Dyn, })
gensym1292 = List(Dyn)
gensym1098 = Function(AnonymousParameters([]), Dyn)
gensym1276 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym203 = Int
gensym1338 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym1113 = Dyn
gensym429 = Dyn
gensym218 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1144 = Dyn
gensym1224 = Function(AnonymousParameters([Dyn]), Dyn)
gensym937 = Dyn
gensym562 = Object('', {'tiles': Dyn, })
gensym357 = Int
gensym966 = Function(DynParameters, Dyn)
gensym886 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1342 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1341 = Dyn
gensym312 = Dyn
gensym954 = Object('', {'already_done': Dyn, })
gensym1138 = Dyn
gensym535 = Dyn
gensym418 = Function(AnonymousParameters([Dyn]), Dyn)
gensym551 = Dyn
gensym246 = Dyn
gensym789 = Dyn
gensym1184 = List(Dyn)
gensym1123 = Dyn
gensym190 = Dyn
gensym951 = Dyn
gensym672 = Object('', {'count': Dyn, })
gensym1007 = Dyn
gensym480 = Dyn
gensym444 = Function(AnonymousParameters([Dyn]), Dyn)
gensym447 = List(Dyn)
gensym1317 = Dyn
gensym915 = String
gensym16 = Int
gensym105 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('v', Int)]), Dyn)
gensym1109 = Dyn
gensym1203 = Dyn
gensym1383 = Dyn
gensym111 = Function(AnonymousParameters([Int]), Dyn)
gensym533 = Dyn
gensym726 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1235 = Dyn
gensym773 = Dyn
gensym1333 = Dyn
gensym1391 = Dyn
gensym1322 = Tuple(Int, Int)
gensym1040 = Object('', {'hex': Dyn, })
gensym696 = Function(AnonymousParameters([Dyn]), Dyn)
gensym620 = Function(AnonymousParameters([Dyn]), Dyn)
gensym248 = Dyn
gensym64 = Dyn
gensym467 = Int
gensym909 = Dyn
gensym336 = Dyn
gensym800 = Function(NamedParameters([('pos', Dyn), ('strategy', Int), ('order', Int)]), Dyn)
gensym1255 = Dyn
gensym571 = Dyn
gensym975 = Dyn
gensym1195 = Dyn
gensym104 = Dyn
gensym188 = Dyn
gensym1309 = Int
gensym1022 = Object('', {'links': Dyn, })
gensym157 = Dyn
gensym978 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym1219 = Dyn
gensym201 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1402 = Function(AnonymousParameters([]), Dyn)
gensym573 = Dyn
gensym622 = Object('', {'hex': Dyn, })
gensym1345 = Dyn
gensym284 = Int
gensym1413 = Function(AnonymousParameters([]), Dyn)
gensym309 = Int
gensym1017 = Dyn
gensym73 = Function(AnonymousParameters([Int]), Dyn)
gensym793 = Bool
gensym22 = Int
gensym466 = Dyn
gensym319 = Function(AnonymousParameters([Dyn]), Dyn)
gensym177 = Int
gensym762 = Dyn
gensym797 = Dyn
gensym927 = Dyn
gensym963 = String
gensym763 = Int
gensym186 = Dyn
gensym1288 = Object('', {'strip': Dyn, })
gensym47 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))]), Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))
gensym378 = Int
gensym841 = Dyn
gensym960 = Dyn
gensym259 = Dyn
gensym1090 = Int
gensym875 = String
gensym1099 = Dyn
gensym687 = Int
gensym408 = Function(NamedParameters([('self', Dyn), ('pos', Dyn), ('id', Dyn), ('links', Dyn)]), Dyn)
gensym289 = Int
gensym828 = Object('', {'next_cell': Dyn, })
gensym189 = Int
gensym1182 = Function(AnonymousParameters([String]), Dyn)
gensym601 = Dyn
gensym985 = Dyn
gensym91 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym1218 = Dyn
gensym78 = Int
gensym976 = Function(DynParameters, Dyn)
gensym1069 = Dyn
gensym299 = Dyn
gensym1221 = Dyn
gensym516 = Object('', {'x': Dyn, })
gensym94 = Dyn
gensym737 = Dyn
gensym1230 = Int
gensym769 = Dyn
gensym869 = Dyn
gensym455 = Dyn
gensym1360 = Function(NamedParameters([('file', Dyn), ('strategy', Int), ('order', Int), ('output', Dyn)]), Dyn)
gensym409 = Dyn
gensym55 = Int
gensym554 = Function(AnonymousParameters([]), Dyn)
gensym368 = Object('', {'next_cell_highest_value': Dyn, })
gensym370 = Function(AnonymousParameters([]), Dyn)
gensym1398 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1033 = Dyn
gensym845 = Dyn
gensym314 = Dyn
gensym634 = Function(AnonymousParameters([Dyn]), Dyn)
gensym693 = Dyn
gensym1396 = Function(AnonymousParameters([]), Dyn)
gensym61 = Dyn
gensym646 = Function(AnonymousParameters([Dyn]), Dyn)
gensym971 = Dyn
gensym884 = Object('', {'get_by_pos': Dyn, })
gensym462 = Object('', {'nodes_by_pos': Dyn, })
gensym791 = Dyn
gensym1059 = Int
gensym760 = Function(AnonymousParameters([Dyn]), Dyn)
gensym399 = Dyn
gensym1393 = Dyn
gensym807 = Dyn
gensym461 = Dyn
gensym469 = Dyn
gensym1257 = Int
gensym996 = Dyn
gensym1382 = Function(AnonymousParameters([Dyn]), Dyn)
gensym184 = Dyn
gensym92 = Dyn
gensym1181 = Dyn
gensym118 = Function(AnonymousParameters([Int]), Dyn)
gensym176 = Dyn
gensym497 = Tuple(Dyn, Dyn)
gensym1024 = Object('', {'hex': Dyn, })
gensym401 = Dyn
gensym973 = String
gensym1310 = Dyn
gensym1307 = Dyn
gensym482 = Dyn
gensym224 = Dyn
gensym801 = Dyn
gensym499 = List(Dyn)
gensym872 = Object('', {'id': Dyn, })
gensym1332 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym1226 = Function(AnonymousParameters([Dyn]), Dyn)
gensym165 = Dyn
gensym101 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('i', Int), ('v', Int)]), Bool)
gensym569 = Dyn
gensym827 = Dyn
gensym950 = Function(AnonymousParameters([Tuple(Dyn, Dyn)]), Dyn)
gensym897 = Dyn
gensym899 = Dyn
gensym817 = Dyn
gensym166 = Function(AnonymousParameters([Int]), Dyn)
gensym745 = Dyn
gensym222 = Int
gensym281 = Dyn
gensym1114 = Int
gensym974 = Dyn
gensym1010 = Object('', {'tiles': Dyn, })
gensym51 = Dyn
gensym1031 = Dyn
gensym63 = Function(AnonymousParameters([Int]), Dyn)
gensym534 = Class('Hex', {'get_by_pos': Function(NamedParameters([('self', TypeVariable('Hex')), ('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'contains_pos': Function(NamedParameters([('self', TypeVariable('Hex')), ('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([('self', TypeVariable('Hex'))]), Dyn), '__init__': Function(NamedParameters([('self', Dyn), ('size', Int)]), Dyn), 'get_by_id': Function(NamedParameters([('self', TypeVariable('Hex')), ('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), }, {'size': Int, 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, })
gensym1248 = Object('', {'strip': Dyn, })
gensym740 = Object('', {'cells': Dyn, })
gensym630 = Object('', {'hex': Dyn, })
gensym1239 = Dyn
gensym217 = Dyn
gensym76 = Dyn
gensym374 = Object('', {'next_cell_min_choice': Dyn, })
gensym830 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym363 = Dyn
gensym1021 = Dyn
gensym1269 = Dyn
gensym593 = Dyn
gensym964 = Dyn
gensym1297 = Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), })
gensym724 = Object('', {'remove_unfixed': Dyn, })
gensym211 = Dyn
gensym844 = Object('', {'append': Dyn, })
gensym25 = Dyn
gensym686 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1378 = Object('', {'getvalue': Dyn, })
gensym5 = Dyn
gensym722 = Object('', {'tiles': Dyn, })
gensym1075 = Dyn
gensym1348 = Tuple(Int, Int)
gensym1130 = Dyn
gensym574 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1045 = Bool
gensym1275 = Dyn
gensym756 = Function(AnonymousParameters([Dyn]), Dyn)
gensym716 = Dyn
gensym326 = Dyn
gensym1262 = Int
gensym560 = Dyn
gensym1227 = Dyn
gensym57 = List(List(Int))
gensym383 = Dyn
gensym1387 = Dyn
gensym654 = Object('', {'count': Dyn, })
gensym498 = Dyn
gensym754 = Object('', {'count': Dyn, })
gensym1397 = Dyn
gensym802 = Object('', {'done': Dyn, })
gensym699 = Dyn
gensym243 = Int
gensym160 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1250 = Function(AnonymousParameters([String]), Dyn)
gensym842 = Function(AnonymousParameters([Dyn]), Dyn)
gensym426 = Object('', {'id': Dyn, })
gensym449 = Dyn
gensym400 = Function(AnonymousParameters([Dyn]), Dyn)
gensym145 = Int
gensym59 = Dyn
gensym136 = Dyn
gensym30 = Bool
gensym337 = Int
gensym1301 = Int
gensym316 = Dyn
gensym629 = Dyn
gensym446 = Dyn
gensym147 = Dyn
gensym423 = Dyn
gensym278 = Object('', {'get_by_id': Dyn, })
gensym240 = Function(AnonymousParameters([Dyn]), Dyn)
gensym301 = Dyn
gensym878 = Dyn
gensym477 = Dyn
gensym6 = Int
gensym199 = Int
gensym1043 = Dyn
gensym1406 = Dyn
gensym784 = Bool
gensym811 = Dyn
gensym40 = Dyn
gensym676 = Object('', {'hex': Dyn, })
gensym264 = Object('', {'get_by_id': Dyn, })
gensym1283 = Dyn
gensym896 = Object('', {'hex': Dyn, })
gensym1245 = Dyn
gensym496 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym36 = Dyn
gensym1162 = Object('', {'count': Dyn, })
gensym990 = Function(AnonymousParameters([Dyn]), Dyn)
gensym141 = Function(AnonymousParameters([Int]), Dyn)
gensym2 = Dyn
gensym382 = Function(AnonymousParameters([]), Dyn)
gensym988 = Function(AnonymousParameters([Dyn]), Dyn)
gensym678 = Object('', {'get_by_id': Dyn, })
gensym286 = Function(AnonymousParameters([Dyn]), Dyn)
gensym262 = Object('', {'hex': Dyn, })
gensym603 = Dyn
gensym586 = Function(AnonymousParameters([Int]), Dyn)
gensym564 = Object('', {'done': Dyn, })
gensym1327 = Dyn
gensym1196 = Function(AnonymousParameters([Dyn]), Dyn)
gensym163 = Int
gensym1302 = Dyn
gensym1136 = Dyn
gensym635 = Dyn
gensym1314 = Dyn
gensym1189 = Dyn
gensym627 = Dyn
gensym1373 = Dyn
gensym369 = Dyn
gensym641 = Dyn
gensym1151 = Object('', {'tiles': Dyn, })
gensym628 = Object('', {'links': Dyn, })
gensym406 = Class('Done', {'next_cell_highest_value': Function(NamedParameters([('self', TypeVariable('Done'))]), Int), 'remove_all': Function(NamedParameters([('self', TypeVariable('Done')), ('v', Int)]), Dyn), 'already_done': Function(NamedParameters([('self', TypeVariable('Done')), ('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('self', TypeVariable('Done')), ('tiles', List(Int))]), Dyn), '__init__': Function(DynParameters, Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([('self', TypeVariable('Done'))]), Int), 'next_cell_min_choice': Function(NamedParameters([('self', TypeVariable('Done'))]), Int), 'set_done': Function(NamedParameters([('self', TypeVariable('Done')), ('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('self', TypeVariable('Done')), ('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('self', TypeVariable('Done')), ('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([('self', TypeVariable('Done'))]), TypeVariable('Done')), 'remove_unfixed': Function(NamedParameters([('self', TypeVariable('Done')), ('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('self', TypeVariable('Done')), ('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('self', TypeVariable('Done')), ('pos', Dyn)]), Int), 'next_cell_first': Function(NamedParameters([('self', TypeVariable('Done'))]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }, {'cells': List(List(Int)), 'count': Int, })
gensym149 = Dyn
gensym1185 = Dyn
gensym1212 = List(Dyn)
gensym1204 = Object('', {'splitlines': Dyn, })
gensym568 = Function(AnonymousParameters([Dyn]), Dyn)
gensym179 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))]), Int)
gensym182 = Dyn
gensym753 = Dyn
gensym907 = Dyn
gensym365 = Int
gensym161 = Int
gensym77 = List(List(Int))
gensym531 = Dyn
gensym265 = Dyn
gensym903 = Dyn
gensym1095 = Dyn
gensym549 = Dyn
gensym1143 = Object('', {'tiles': Dyn, })
gensym493 = Dyn
gensym1079 = Dyn
gensym1284 = Object('', {'splitlines': Dyn, })
gensym41 = Function(AnonymousParameters([Dyn]), Dyn)
gensym782 = Dyn
gensym196 = Dyn
gensym1050 = Object('', {'count': Dyn, })
gensym689 = Int
gensym320 = Dyn
gensym1102 = Int
gensym43 = List(List(Int))
gensym1419 = Dyn
gensym54 = Dyn
gensym1167 = Dyn
gensym170 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym547 = Dyn
gensym1316 = Function(AnonymousParameters([Dyn]), Dyn)
gensym425 = Dyn
gensym414 = Object('', {'count': Dyn, })
gensym164 = Dyn
gensym1159 = Dyn
gensym1092 = Object('', {'clone': Dyn, })
gensym1233 = Dyn
gensym1111 = Dyn
gensym10 = Int
gensym342 = Int
gensym438 = Object('', {'id': Dyn, })
gensym14 = Int
gensym865 = Dyn
gensym785 = Dyn
gensym743 = Dyn
gensym155 = Dyn
gensym638 = Function(AnonymousParameters([Int]), Dyn)
gensym1001 = Function(DynParameters, Dyn)
gensym607 = Dyn
gensym518 = Object('', {'y': Dyn, })
gensym1004 = Function(DynParameters, Int)
gensym747 = Dyn
gensym442 = Function(AnonymousParameters([Int]), Dyn)
gensym1093 = Dyn
gensym490 = Dyn
gensym404 = Function(AnonymousParameters([Dyn]), Dyn)
gensym23 = Dyn
gensym920 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym1272 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym15 = Dyn
gensym1216 = Int
gensym1047 = Bool
gensym1015 = Dyn
gensym1328 = Int
gensym27 = Dyn
gensym212 = Function(AnonymousParameters([Int]), Dyn)
gensym1367 = Dyn
gensym230 = Dyn
gensym561 = Dyn
gensym215 = List(Int)
gensym366 = Dyn
gensym169 = Dyn
gensym1096 = Object('', {'clone': Dyn, })
gensym479 = Tuple(Dyn, Dyn)
gensym354 = Dyn
gensym1238 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1149 = Object('', {'hex': Dyn, })
gensym757 = Dyn
gensym121 = Bool
gensym647 = Dyn
gensym544 = Function(NamedParameters([('self', Dyn)]), Dyn)
gensym563 = Dyn
gensym250 = Dyn
gensym1408 = Dyn
gensym1313 = Int
gensym994 = Dyn
gensym597 = Dyn
gensym388 = Function(AnonymousParameters([]), Dyn)
gensym1335 = Int
gensym416 = Function(AnonymousParameters([Int]), Dyn)
gensym434 = Object('', {'nodes_by_pos': Dyn, })
gensym1207 = Dyn
gensym822 = Function(AnonymousParameters([List(Tuple(Dyn, Dyn))]), Dyn)
gensym334 = Dyn
gensym1086 = Function(AnonymousParameters([]), Dyn)
gensym979 = Dyn
gensym1161 = Dyn
gensym631 = Dyn
gensym596 = Object('', {'count': Dyn, })
gensym407 = Dyn
gensym530 = Function(NamedParameters([('self', Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), })), ('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, }))
gensym12 = Int
gensym276 = Object('', {'hex': Dyn, })
gensym1053 = Dyn
gensym984 = Object('', {'id': Dyn, })
gensym465 = Int
gensym590 = Function(AnonymousParameters([Int]), Dyn)
gensym343 = Dyn
gensym665 = Bool
gensym677 = Dyn
gensym1379 = Dyn
gensym639 = Dyn
gensym474 = Dyn
gensym348 = Dyn
gensym113 = Int
gensym1094 = Function(AnonymousParameters([]), Dyn)
gensym1087 = Dyn
gensym1107 = Dyn
gensym229 = Int
gensym992 = Dyn
gensym1390 = Function(AnonymousParameters([]), Dyn)
gensym776 = Function(AnonymousParameters([Dyn]), Dyn)
gensym721 = Dyn
gensym831 = List(Dyn)
gensym1165 = Dyn
gensym273 = Dyn
gensym132 = Dyn
gensym443 = Dyn
gensym521 = Tuple(Dyn, Dyn)
gensym1209 = Dyn
gensym1014 = Object('', {'count': Dyn, })
gensym358 = Dyn
gensym1236 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym349 = Object('', {'hex': Dyn, })
gensym1414 = Dyn
gensym725 = Dyn
gensym1199 = Dyn
gensym744 = Function(AnonymousParameters([Dyn]), Dyn)
gensym799 = Dyn
gensym1305 = Dyn
gensym889 = Dyn
gensym948 = Object('', {'get_by_pos': Dyn, })
gensym882 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym413 = Dyn
gensym894 = Dyn
gensym787 = Dyn
gensym1016 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1229 = Dyn
gensym220 = Function(AnonymousParameters([Int]), Dyn)
gensym1026 = Object('', {'tiles': Dyn, })
gensym1183 = Dyn
gensym1311 = Dyn
gensym494 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym643 = Dyn
gensym1141 = Object('', {'hex': Dyn, })
gensym58 = Int
gensym315 = Object('', {'hex': Dyn, })
gensym263 = Dyn
gensym1106 = Function(AnonymousParameters([]), Dyn)
gensym341 = Dyn
gensym75 = Int
gensym806 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym333 = Function(AnonymousParameters([Dyn]), Dyn)
gensym790 = Object('', {'remove': Dyn, })
gensym505 = Dyn
gensym527 = Dyn
gensym279 = Dyn
gensym701 = Dyn
gensym98 = Dyn
gensym1178 = Function(AnonymousParameters([]), Dyn)
gensym1240 = Int
gensym1344 = Int
gensym912 = Function(AnonymousParameters([Dyn]), Dyn)
gensym375 = Dyn
gensym1282 = Int
gensym236 = Int
gensym1220 = Function(AnonymousParameters([Dyn]), Dyn)
gensym445 = Tuple(Dyn, Dyn)
gensym29 = Function(DynParameters, Dyn)
gensym1145 = Object('', {'done': Dyn, })
gensym1188 = Int
gensym1163 = Dyn
gensym1208 = Object('', {'strip': Dyn, })
gensym741 = Dyn
gensym669 = Dyn
gensym478 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1304 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Dyn), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Dyn), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym379 = Dyn
gensym730 = Object('', {'cells': Dyn, })
gensym1150 = Dyn
gensym904 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1193 = Dyn
gensym860 = Object('', {'done': Dyn, })
gensym959 = String
gensym612 = Object('', {'links': Dyn, })
gensym566 = Object('', {'count': Dyn, })
gensym1062 = Dyn
gensym324 = Dyn
gensym441 = Dyn
gensym1405 = Dyn
gensym1266 = Function(AnonymousParameters([Dyn]), Dyn)
gensym901 = Dyn
gensym685 = Dyn
gensym1223 = Dyn
gensym487 = Dyn
gensym1353 = Dyn
gensym764 = Dyn
gensym1222 = Int
gensym322 = Dyn
gensym402 = Int
gensym1385 = Dyn
gensym106 = Dyn
gensym1370 = Dyn
gensym1140 = Dyn
gensym766 = Object('', {'hex': Dyn, })
gensym1187 = Dyn
gensym1076 = Bool
gensym81 = Dyn
gensym1171 = Int
gensym72 = Dyn
gensym507 = Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })
gensym749 = Bool
gensym46 = Dyn
gensym463 = Dyn
gensym854 = Function(AnonymousParameters([Int, Int]), Dyn)
gensym456 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym956 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1372 = Int
gensym723 = Dyn
gensym1399 = Dyn
gensym376 = Function(AnonymousParameters([]), Dyn)
gensym1155 = Dyn
gensym1231 = Dyn
gensym1334 = Int
gensym614 = Object('', {'tiles': Dyn, })
gensym913 = String
gensym734 = Object('', {'tiles': Dyn, })
gensym130 = Dyn
gensym210 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))]), Int)
gensym859 = Dyn
gensym1359 = Dyn
gensym968 = Dyn
gensym308 = Dyn
gensym640 = Object('', {'cells': Dyn, })
gensym1298 = Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Dyn), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), })
gensym1289 = Dyn
gensym746 = Object('', {'set_done': Dyn, })
gensym758 = Object('', {'already_done': Dyn, })
gensym1127 = Int
gensym644 = Object('', {'cells': Dyn, })
gensym1205 = Dyn
gensym267 = Dyn
gensym1038 = Object('', {'links': Dyn, })
gensym44 = List(Dyn)
gensym702 = Function(AnonymousParameters([Dyn]), Dyn)
gensym649 = Dyn
gensym728 = Dyn
gensym615 = Dyn
gensym890 = Function(AnonymousParameters([Dyn]), Dyn)
gensym835 = List(Tuple(Dyn, Dyn))
gensym885 = Dyn
gensym112 = Dyn
gensym1158 = Int
gensym329 = Object('', {'hex': Dyn, })
gensym1011 = Dyn
gensym88 = Dyn
gensym998 = Function(DynParameters, Dyn)
gensym1003 = Dyn
gensym868 = Object('', {'get_by_pos': Dyn, })
gensym925 = Dyn
gensym610 = Function(AnonymousParameters([Dyn]), Dyn)
gensym33 = Function(AnonymousParameters([Dyn]), Dyn)
gensym989 = Dyn
gensym296 = Object('', {'hex': Dyn, })
gensym849 = Dyn
gensym991 = String
gensym772 = Object('', {'links': Dyn, })
gensym508 = Dyn
gensym767 = Dyn
gensym856 = Function(NamedParameters([('pos', Dyn), ('output', Dyn)]), Dyn)
gensym1273 = Dyn
gensym539 = Dyn
gensym1194 = Function(AnonymousParameters([Dyn]), Dyn)
gensym283 = Dyn
gensym580 = Object('', {'get_by_id': Dyn, })
gensym935 = Dyn
gensym364 = Function(DynParameters, Int)
gensym1124 = Tuple(Int, Int)
gensym599 = Dyn
gensym578 = Object('', {'hex': Dyn, })
gensym595 = Dyn
gensym673 = Dyn
gensym1081 = Bool
gensym541 = Dyn
gensym472 = Dyn
gensym484 = Object('', {'nodes_by_pos': Dyn, })
gensym1044 = Object('', {'done': Dyn, })
gensym550 = Object('', {'done': Dyn, })
gensym809 = Dyn
gensym781 = Object('', {'set_done': Dyn, })
gensym609 = Dyn
gensym481 = List(Dyn)
gensym32 = Dyn
gensym675 = Dyn
gensym295 = Dyn
gensym19 = Dyn
gensym1251 = Dyn
gensym663 = Dyn
gensym824 = Function(AnonymousParameters([Dyn]), Dyn)
gensym317 = Object('', {'get_by_id': Dyn, })
gensym1286 = Function(AnonymousParameters([]), Dyn)
gensym933 = Dyn
gensym729 = Dyn
gensym1028 = Object('', {'done': Dyn, })
gensym1215 = Dyn
gensym515 = Dyn
gensym742 = Object('', {'already_done': Dyn, })
gensym208 = Int
gensym28 = Dyn
gensym50 = Bool
gensym151 = Dyn
gensym605 = Dyn
gensym826 = Object('', {'done': Dyn, })
gensym1000 = Dyn
gensym581 = Dyn
gensym816 = Object('', {'next_cell': Dyn, })
gensym755 = Dyn
gensym738 = Function(AnonymousParameters([Dyn]), Dyn)
gensym924 = Function(AnonymousParameters([Tuple(Dyn, Dyn)]), Dyn)
gensym1267 = Dyn
gensym582 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1225 = Dyn
gensym661 = Dyn
gensym331 = Object('', {'get_by_id': Dyn, })
gensym668 = Object('', {'tiles': Dyn, })
gensym460 = Dyn
gensym1234 = Int
gensym1365 = Dyn
gensym1376 = Function(AnonymousParameters([]), Dyn)
gensym846 = Function(AnonymousParameters([Tuple(Dyn, Int)]), Dyn)
gensym710 = Bool
gensym1371 = Dyn
gensym1097 = Dyn
gensym1401 = Dyn
gensym167 = Dyn
gensym42 = Dyn
gensym815 = Dyn
gensym237 = List(Int)
gensym1363 = Dyn
gensym1139 = Function(AnonymousParameters([Int]), Dyn)
gensym266 = Function(AnonymousParameters([Dyn]), Dyn)
gensym187 = Function(AnonymousParameters([Int]), Dyn)
gensym99 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1281 = Dyn
gensym126 = Int
gensym340 = Int
gensym431 = List(Dyn)
gensym1291 = Dyn
gensym1067 = Dyn
gensym848 = Function(NamedParameters([('pos', Dyn), ('move', Tuple(Int, Int))]), Dyn)
gensym1108 = Object('', {'clone': Dyn, })
gensym1357 = Dyn
gensym1299 = Int
gensym1380 = Function(AnonymousParameters([]), Dyn)
gensym1118 = Dyn
gensym1306 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1089 = Dyn
gensym403 = Dyn
gensym96 = Dyn
gensym523 = Tuple(Dyn, Dyn)
gensym86 = Dyn
gensym37 = Function(AnonymousParameters([Dyn]), Dyn)
gensym871 = Dyn
gensym464 = Object('', {'nodes_by_id': Dyn, })
gensym373 = Dyn
gensym1350 = Function(AnonymousParameters([String]), Dyn)
gensym1186 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1412 = Dyn
gensym235 = Dyn
gensym1211 = Dyn
gensym148 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))]), Int)
gensym488 = Object('', {'nodes_by_id': Dyn, })
gensym587 = Dyn
gensym911 = Dyn
gensym1252 = List(Dyn)
gensym642 = Function(AnonymousParameters([Int]), Dyn)
gensym736 = Object('', {'count': Dyn, })
gensym1055 = Dyn
gensym502 = Object('', {'nodes_by_pos': Dyn, })
gensym245 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, }))]), Int)
gensym372 = Int
gensym433 = Dyn
gensym74 = Dyn
gensym1005 = Bool
gensym313 = Function(AnonymousParameters([Int]), Dyn)
gensym528 = Function(NamedParameters([('self', Object('Hex', {'nodes_by_id': List(Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'count': Int, 'get_by_id': Function(NamedParameters([('id', Int)]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'size': Int, 'contains_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Bool), 'link_nodes': Function(NamedParameters([]), Dyn), 'get_by_pos': Function(NamedParameters([('pos', Tuple(Int, Int))]), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), 'nodes_by_pos': Dict(Tuple(Int, Int), Object('Node', {'links': List(Int), 'id': Int, 'pos': Dyn, })), })), ('pos', Tuple(Int, Int))]), Bool)
gensym555 = Dyn
gensym733 = Dyn
gensym1206 = Function(AnonymousParameters([]), Dyn)
gensym866 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1104 = Object('', {'clone': Dyn, })
gensym1039 = Dyn
gensym952 = Object('', {'id': Dyn, })
gensym778 = Dyn
gensym252 = Dyn
gensym652 = Object('', {'cells': Dyn, })
gensym621 = Dyn
gensym68 = Int
gensym616 = Object('', {'done': Dyn, })
gensym65 = Int
gensym648 = Object('', {'count': Dyn, })
gensym1157 = Function(AnonymousParameters([Int]), Dyn)
gensym825 = Dyn
gensym977 = Dyn
gensym748 = Function(AnonymousParameters([Dyn, Dyn]), Dyn)
gensym143 = Int
gensym432 = Dyn
gensym876 = Dyn
gensym570 = Object('', {'hex': Dyn, })
gensym692 = Object('', {'hex': Dyn, })
gensym330 = Dyn
gensym158 = Int
gensym48 = Int
gensym944 = Function(DynParameters, Dyn)
gensym958 = Function(AnonymousParameters([Dyn]), Dyn)
gensym819 = Dyn
gensym706 = Dyn
gensym346 = Dyn
gensym1084 = Object('', {'clone': Dyn, })
gensym470 = Object('', {'count': Dyn, })
gensym619 = Dyn
gensym537 = Void
gensym45 = Dyn
gensym697 = Dyn
gensym945 = Dyn
gensym3 = Class('Dir', {'__init__': Function(NamedParameters([('self', Dyn), ('x', Dyn), ('y', Dyn)]), Dyn), }, {'x': Int, 'y': Int, })
gensym947 = Dyn
gensym932 = Dyn
gensym1121 = Dyn
gensym395 = Dyn
gensym881 = Dyn
gensym285 = Dyn
gensym1153 = Object('', {'done': Dyn, })
gensym1400 = Function(AnonymousParameters([]), Dyn)
gensym66 = Dyn
gensym1369 = String
gensym202 = Dyn
gensym1249 = Dyn
gensym327 = Function(AnonymousParameters([Int]), Dyn)
gensym783 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym60 = Bool
gensym1287 = Dyn
gensym344 = Dyn
gensym788 = Function(AnonymousParameters([List(Dyn)]), Dyn)
gensym1175 = Dyn
gensym120 = Function(AnonymousParameters([Int]), Dyn)
gensym1259 = Dyn
gensym290 = Dyn
gensym1312 = Function(AnonymousParameters([Dyn]), Dyn)
gensym39 = List(List(Int))
gensym934 = Object('', {'hex': Dyn, })
gensym1064 = Object('', {'get_by_id': Dyn, })
gensym887 = Dyn
gensym35 = List(List(Int))
gensym943 = Dyn
gensym294 = Int
gensym1128 = Dyn
gensym213 = Dyn
gensym808 = List(Tuple(Dyn, Dyn))
gensym1198 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym955 = Dyn
gensym1120 = Object('', {'clone': Dyn, })
gensym1032 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1243 = Dyn
gensym216 = Dyn
gensym719 = Dyn
gensym137 = Function(AnonymousParameters([Int]), Dyn)
gensym394 = Function(AnonymousParameters([Dyn]), Dyn)
gensym818 = Function(AnonymousParameters([Dyn, Int]), Dyn)
gensym1009 = Dyn
gensym1041 = Dyn
gensym546 = Object('', {'hex': Dyn, })
gensym1258 = Dyn
gensym1256 = Int
gensym178 = Dyn
gensym1270 = Int
gensym617 = Dyn
gensym594 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1057 = Dyn
gensym1177 = Dyn
gensym558 = Function(DynParameters, Bool)
gensym356 = Dyn
gensym486 = Dyn
gensym1324 = Function(AnonymousParameters([String]), Dyn)
gensym119 = Dyn
gensym1115 = Dyn
gensym198 = Dyn
gensym1018 = Object('', {'get_by_id': Dyn, })
gensym1254 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1361 = Dyn
gensym181 = Function(AnonymousParameters([Int]), Dyn)
gensym255 = Int
gensym1166 = Function(AnonymousParameters([String]), Dyn)
gensym1060 = Dyn
gensym9 = Dyn
gensym339 = Function(AnonymousParameters([Dyn]), Dyn)
gensym159 = Dyn
gensym140 = Dyn
gensym732 = Function(AnonymousParameters([Dyn]), Dyn)
gensym770 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1293 = Dyn
gensym310 = Dyn
gensym888 = Object('', {'id': Dyn, })
gensym225 = Dyn
gensym298 = Object('', {'get_by_id': Dyn, })
gensym107 = Function(AnonymousParameters([Int]), Dyn)
gensym1290 = Function(AnonymousParameters([String]), Dyn)
gensym650 = Function(AnonymousParameters([Dyn]), Dyn)
gensym1126 = Dyn
gensym1416 = Int
gensym1228 = Int
gensym242 = Dyn
gensym691 = Dyn
gensym536 = Function(DynParameters, Dyn)
gensym282 = Object('', {'links': Dyn, })
gensym1340 = Dyn
gensym891 = String
gensym577 = Dyn
gensym1253 = Dyn
gensym812 = Function(AnonymousParameters([Dyn]), Dyn)
gensym731 = Dyn
gensym969 = Function(DynParameters, Dyn)
gensym352 = Dyn
gensym1034 = Object('', {'get_by_id': Dyn, })
gensym1152 = Dyn
gensym1054 = Function(AnonymousParameters([Dyn]), Dyn)
gensym162 = Dyn
gensym814 = Object('', {'done': Dyn, })
gensym513 = Dyn
gensym662 = Function(AnonymousParameters([Dyn]), Dyn)
gensym679 = Dyn
gensym946 = Function(AnonymousParameters([Dyn]), Dyn)
gensym293 = Dyn
gensym520 = Tuple(Dyn, Dyn)
gensym1346 = Int
gensym982 = Function(AnonymousParameters([Tuple(Dyn, Dyn)]), Dyn)
gensym350 = Dyn
gensym1066 = Function(AnonymousParameters([Dyn]), Dyn)
gensym840 = Function(AnonymousParameters([List(Tuple(Dyn, Dyn))]), Dyn)
gensym410 = Class('Node', {'__init__': Function(NamedParameters([('self', Dyn), ('pos', Dyn), ('id', Dyn), ('links', Dyn)]), Dyn), }, {'links': List(Int), 'id': Int, 'pos': Dyn, })
gensym116 = Function(NamedParameters([('self', Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })), ('v', Int)]), Bool)
gensym565 = Dyn
gensym124 = Function(AnonymousParameters([Int]), Dyn)
gensym11 = Dyn
gensym821 = Dyn
gensym862 = Object('', {'size': Dyn, })
gensym191 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym1366 = Function(AnonymousParameters([]), Dyn)
gensym880 = Function(AnonymousParameters([Int, Dyn]), Dyn)
gensym1339 = Int
gensym244 = Dyn
gensym405 = Dyn
gensym389 = Dyn
gensym90 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'next_cell': Function(DynParameters, Int), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'already_done': Function(NamedParameters([('i', Int)]), Dyn), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Dyn), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym223 = List(Int)
gensym377 = Dyn
gensym500 = Dyn
gensym681 = Dyn
gensym393 = Dyn
gensym501 = Dyn
gensym483 = Dyn
gensym83 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'already_done': Function(NamedParameters([('i', Int)]), Dyn), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'next_cell': Function(DynParameters, Int), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Dyn), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym1 = Function(NamedParameters([('self', Dyn), ('x', Dyn), ('y', Dyn)]), Dyn)
gensym269 = Dyn
gensym459 = List(Dyn)
gensym417 = Dyn
gensym458 = Dyn
gensym205 = Function(AnonymousParameters([List(Int)]), Dyn)
gensym949 = Dyn
gensym519 = Dyn
gensym332 = Dyn
gensym1142 = Dyn
gensym1280 = Int
gensym759 = Dyn
gensym1303 = Object('Done', {'next_cell_highest_value': Function(NamedParameters([]), Int), 'count': Int, 'next_cell': Function(DynParameters, Int), 'filter_tiles': Function(NamedParameters([('tiles', List(Int))]), Dyn), 'already_done': Function(NamedParameters([('i', Int)]), Bool), 'HIGHEST_VALUE_STRATEGY': Dyn, 'next_cell_max_choice': Function(NamedParameters([]), Int), 'next_cell_min_choice': Function(NamedParameters([]), Int), 'set_done': Function(NamedParameters([('i', Int), ('v', Int)]), Dyn), '__getitem__': Function(NamedParameters([('i', Int)]), List(Int)), 'MIN_CHOICE_STRATEGY': Dyn, 'remove': Function(NamedParameters([('i', Int), ('v', Int)]), Bool), 'clone': Function(NamedParameters([]), TypeVariable('Done')), 'remove_all': Function(NamedParameters([('v', Int)]), Dyn), 'remove_unfixed': Function(NamedParameters([('v', Int)]), Bool), 'next_cell_max_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'next_cell_min_neighbors': Function(NamedParameters([('pos', Dyn)]), Int), 'cells': List(List(Int)), 'next_cell_first': Function(NamedParameters([]), Int), 'MAX_CHOICE_STRATEGY': Dyn, 'FIRST_STRATEGY': Dyn, 'MAX_NEIGHBORS_STRATEGY': Dyn, 'MIN_NEIGHBORS_STRATEGY': Dyn, })
gensym857 = Dyn
gensym1364 = Function(AnonymousParameters([]), Dyn)
import sys
import time
from compat import StringIO, u_lit, unicode, xrange


class Dir(retic_actual(object)):

    def __init__(self, x, y):
        self.x = x
        self.y = y
Dir = mgd_cast_type_class(Dir, gensym2, '15', gensym3, ['__init__'])
DIRS = [check0(Dir(mgd_cast_type_dyn(1, gensym4, '21', gensym5), mgd_cast_type_dyn(0, gensym6, '21', gensym7)), Dir, 2), check0(Dir(mgd_cast_type_dyn((- 1), gensym8, '22', gensym9), mgd_cast_type_dyn(0, gensym10, '22', gensym11)), Dir, 2), check0(Dir(mgd_cast_type_dyn(0, gensym12, '23', gensym13), mgd_cast_type_dyn(1, gensym14, '23', gensym15)), Dir, 2), check0(Dir(mgd_cast_type_dyn(0, gensym16, '24', gensym17), mgd_cast_type_dyn((- 1), gensym18, '24', gensym19)), Dir, 2), check0(Dir(mgd_cast_type_dyn(1, gensym20, '25', gensym21), mgd_cast_type_dyn(1, gensym22, '25', gensym23)), Dir, 2), check0(Dir(mgd_cast_type_dyn((- 1), gensym24, '26', gensym25), mgd_cast_type_dyn((- 1), gensym26, '26', gensym27)), Dir, 2)]
EMPTY = 7


class Done(retic_actual(object)):
    MIN_CHOICE_STRATEGY = 0
    MAX_CHOICE_STRATEGY = 1
    HIGHEST_VALUE_STRATEGY = 2
    FIRST_STRATEGY = 3
    MAX_NEIGHBORS_STRATEGY = 4
    MIN_NEIGHBORS_STRATEGY = 5

    def __init__(self, count, empty=mgd_cast_type_dyn(False, gensym30, '40', gensym31)):
        self.count = count
        self.cells = mgd_cast_type_dyn(([] if empty else mgd_cast_type_list([[0, 1, 2, 3, 4, 5, 6, EMPTY] for i in mgd_cast_type_function(xrange, gensym40, '42', gensym41)(count)], gensym42, '42', gensym43)), gensym44, '42', gensym45)

    def clone(self):
        check1(self, self.clone, (1, 0))
        ret = cast2(check1(Done(mgd_cast_type_dyn(mgd_check_type_int(self.count, self, (0, 'count')), gensym78, '46', gensym79), mgd_cast_type_dyn(True, gensym80, '46', gensym81)), Done, 2), gensym82, '46', gensym83)
        ret.cells = mgd_cast_type_list([mgd_check_type_list(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym86, '47', gensym87)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3)[:], mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym86, '47', gensym87)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3), 3) for i in mgd_cast_type_function(xrange, gensym84, '47', gensym85)(mgd_check_type_int(self.count, self, (0, 'count')))], gensym88, '47', gensym89)
        return cast2(ret, gensym90, '48', gensym91)

    def __getitem__(self, i):
        check1(self, self.__getitem__, (1, 0))
        mgd_check_type_int(i, self.__getitem__, (1, 1))
        return mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[i], mgd_check_type_list(self.cells, self, (0, 'cells')), 3)

    def set_done(self, i, v):
        check1(self, self.set_done, (1, 0))
        mgd_check_type_int(i, self.set_done, (1, 1))
        mgd_check_type_int(v, self.set_done, (1, 2))
        mgd_check_type_list(self.cells, self, (0, 'cells'))[i] = [v]

    def already_done(self, i):
        check1(self, self.already_done, (1, 0))
        mgd_check_type_int(i, self.already_done, (1, 1))
        return (mgd_cast_type_function(len, gensym98, '57', gensym99)(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[i], mgd_check_type_list(self.cells, self, (0, 'cells')), 3)) == 1)

    def remove(self, i, v):
        check1(self, self.remove, (1, 0))
        mgd_check_type_int(i, self.remove, (1, 1))
        mgd_check_type_int(v, self.remove, (1, 2))
        if (v in mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[i], mgd_check_type_list(self.cells, self, (0, 'cells')), 3)):
            mgd_cast_type_function(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[i], mgd_check_type_list(self.cells, self, (0, 'cells')), 3).remove, gensym102, '61', gensym103)(v)
            return True
        else:
            return False

    def remove_all(self, v):
        check1(self, self.remove_all, (1, 0))
        mgd_check_type_int(v, self.remove_all, (1, 1))
        gensym114 = mgd_cast_type_function(xrange, gensym110, '67', gensym111)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym114:
            mgd_check_type_bool(mgd_check_type_function(self.remove, self, (0, 'remove'))(mgd_cast_type_int(i, gensym112, '68', gensym113), v), mgd_check_type_function(self.remove, self, (0, 'remove')), 2)

    def remove_unfixed(self, v):
        check1(self, self.remove_unfixed, (1, 0))
        mgd_check_type_int(v, self.remove_unfixed, (1, 1))
        changed = mgd_cast_type_dyn(False, gensym121, '71', gensym122)
        gensym131 = mgd_cast_type_function(xrange, gensym123, '72', gensym124)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym131:
            if (not mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(i, gensym125, '73', gensym126)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2)):
                if mgd_check_type_bool(mgd_check_type_function(self.remove, self, (0, 'remove'))(mgd_cast_type_int(i, gensym127, '74', gensym128), v), mgd_check_type_function(self.remove, self, (0, 'remove')), 2):
                    changed = mgd_cast_type_dyn(True, gensym129, '75', gensym130)
        return mgd_cast_type_bool(changed, gensym132, '76', gensym133)

    def filter_tiles(self, tiles):
        check1(self, self.filter_tiles, (1, 0))
        mgd_check_type_list(tiles, self.filter_tiles, (1, 1))
        gensym146 = mgd_cast_type_function(xrange, gensym140, '79', gensym141)(8)
        for v in gensym146:
            if (mgd_check_type_int(tiles[mgd_cast_type_int(v, gensym142, '80', gensym143)], tiles, 3) == 0):
                mgd_check_type_function(self.remove_all, self, (0, 'remove_all'))(mgd_cast_type_int(v, gensym144, '81', gensym145))

    def next_cell_min_choice(self):
        check1(self, self.next_cell_min_choice, (1, 0))
        minlen = mgd_cast_type_dyn(10, gensym161, '84', gensym162)
        mini = mgd_cast_type_dyn((- 1), gensym163, '85', gensym164)
        gensym175 = mgd_cast_type_function(xrange, gensym165, '86', gensym166)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym175:
            if (1 < mgd_cast_type_function(len, gensym169, '87', gensym170)(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym167, '87', gensym168)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3)) < minlen):
                minlen = mgd_cast_type_function(len, gensym173, '88', gensym174)(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym171, '88', gensym172)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3))
                mini = i
        return mgd_cast_type_int(mini, gensym176, '90', gensym177)

    def next_cell_max_choice(self):
        check1(self, self.next_cell_max_choice, (1, 0))
        maxlen = mgd_cast_type_dyn(1, gensym192, '93', gensym193)
        maxi = mgd_cast_type_dyn((- 1), gensym194, '94', gensym195)
        gensym206 = mgd_cast_type_function(xrange, gensym196, '95', gensym197)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym206:
            if (maxlen < mgd_cast_type_function(len, gensym200, '96', gensym201)(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym198, '96', gensym199)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3))):
                maxlen = mgd_cast_type_function(len, gensym204, '97', gensym205)(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym202, '97', gensym203)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3))
                maxi = i
        return mgd_cast_type_int(maxi, gensym207, '99', gensym208)

    def next_cell_highest_value(self):
        check1(self, self.next_cell_highest_value, (1, 0))
        maxval = mgd_cast_type_dyn((- 1), gensym227, '102', gensym228)
        maxi = mgd_cast_type_dyn((- 1), gensym229, '103', gensym230)
        gensym241 = mgd_cast_type_function(xrange, gensym231, '104', gensym232)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym241:
            if (not mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(i, gensym233, '105', gensym234)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2)):
                maxvali = mgd_cast_type_function(max, gensym239, '106', gensym240)((k for k in mgd_cast_type_dyn(mgd_check_type_list(mgd_check_type_list(self.cells, self, (0, 'cells'))[mgd_cast_type_int(i, gensym235, '106', gensym236)], mgd_check_type_list(self.cells, self, (0, 'cells')), 3), gensym237, '106', gensym238) if (k != EMPTY)))
                if (maxval < maxvali):
                    maxval = maxvali
                    maxi = i
        return mgd_cast_type_int(maxi, gensym242, '110', gensym243)

    def next_cell_first(self):
        check1(self, self.next_cell_first, (1, 0))
        gensym256 = mgd_cast_type_function(xrange, gensym250, '113', gensym251)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym256:
            if (not mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(i, gensym252, '114', gensym253)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2)):
                return mgd_cast_type_int(i, gensym254, '115', gensym255)
        return (- 1)

    def next_cell_max_neighbors(self, pos):
        check1(self, self.next_cell_max_neighbors, (1, 0))
        maxn = mgd_cast_type_dyn((- 1), gensym287, '119', gensym288)
        maxi = mgd_cast_type_dyn((- 1), gensym289, '120', gensym290)
        gensym307 = mgd_cast_type_function(xrange, gensym291, '121', gensym292)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym307:
            if (not mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(i, gensym293, '122', gensym294)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2)):
                cells_around = cast5(mgd_cast_type_function(cast4(cast3(pos, gensym295, '123', gensym296).hex, gensym297, '123', gensym298).get_by_id, gensym299, '123', gensym300)(i), gensym301, '123', gensym302).links
                n = mgd_cast_type_function(sum, gensym305, '124', gensym306)(((1 if (mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(nid, gensym303, '124', gensym304)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n > maxn):
                    maxn = n
                    maxi = i
        return mgd_cast_type_int(maxi, gensym308, '129', gensym309)

    def next_cell_min_neighbors(self, pos):
        check1(self, self.next_cell_min_neighbors, (1, 0))
        minn = mgd_cast_type_dyn(7, gensym340, '132', gensym341)
        mini = mgd_cast_type_dyn((- 1), gensym342, '133', gensym343)
        gensym360 = mgd_cast_type_function(xrange, gensym344, '134', gensym345)(mgd_check_type_int(self.count, self, (0, 'count')))
        for i in gensym360:
            if (not mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(i, gensym346, '135', gensym347)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2)):
                cells_around = cast5(mgd_cast_type_function(cast4(cast3(pos, gensym348, '136', gensym349).hex, gensym350, '136', gensym351).get_by_id, gensym352, '136', gensym353)(i), gensym354, '136', gensym355).links
                n = mgd_cast_type_function(sum, gensym358, '137', gensym359)(((1 if (mgd_check_type_bool(mgd_check_type_function(self.already_done, self, (0, 'already_done'))(mgd_cast_type_int(nid, gensym356, '137', gensym357)), mgd_check_type_function(self.already_done, self, (0, 'already_done')), 2) and (self[nid][0] != EMPTY)) else 0) for nid in cells_around))
                if (n < minn):
                    minn = n
                    mini = i
        return mgd_cast_type_int(mini, gensym361, '142', gensym362)

    def next_cell(self, pos, strategy=mgd_cast_type_dyn(HIGHEST_VALUE_STRATEGY, gensym365, '145', gensym366)):
        if (strategy == Done.HIGHEST_VALUE_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast6(self, gensym367, '147', gensym368).next_cell_highest_value, gensym369, '147', gensym370)(), gensym371, '147', gensym372)
        elif (strategy == Done.MIN_CHOICE_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast7(self, gensym373, '149', gensym374).next_cell_min_choice, gensym375, '149', gensym376)(), gensym377, '149', gensym378)
        elif (strategy == Done.MAX_CHOICE_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast8(self, gensym379, '151', gensym380).next_cell_max_choice, gensym381, '151', gensym382)(), gensym383, '151', gensym384)
        elif (strategy == Done.FIRST_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast9(self, gensym385, '153', gensym386).next_cell_first, gensym387, '153', gensym388)(), gensym389, '153', gensym390)
        elif (strategy == Done.MAX_NEIGHBORS_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast10(self, gensym391, '155', gensym392).next_cell_max_neighbors, gensym393, '155', gensym394)(pos), gensym395, '155', gensym396)
        elif (strategy == Done.MIN_NEIGHBORS_STRATEGY):
            return mgd_cast_type_int(mgd_cast_type_function(cast11(self, gensym397, '157', gensym398).next_cell_min_neighbors, gensym399, '157', gensym400)(pos), gensym401, '157', gensym402)
        else:
            raise mgd_cast_type_function(Exception, gensym403, '159', gensym404)(('Wrong strategy: %d' % strategy))
Done = mgd_cast_type_class(Done, gensym405, '31', gensym406, ['next_cell_highest_value', 'remove_all', 'already_done', 'filter_tiles', '__init__', 'next_cell', 'HIGHEST_VALUE_STRATEGY', 'next_cell_max_choice', 'next_cell_min_choice', 'set_done', '__getitem__', 'MIN_CHOICE_STRATEGY', 'remove', 'clone', 'remove_unfixed', 'next_cell_max_neighbors', 'next_cell_min_neighbors', 'next_cell_first', 'MAX_CHOICE_STRATEGY', 'FIRST_STRATEGY', 'MAX_NEIGHBORS_STRATEGY', 'MIN_NEIGHBORS_STRATEGY'])


class Node(retic_actual(object)):

    def __init__(self, pos, id, links):
        self.pos = pos
        self.id = id
        self.links = links
Node = mgd_cast_type_class(Node, gensym409, '162', gensym410, ['__init__'])


class Hex(retic_actual(object)):

    def __init__(self, size):
        mgd_check_type_int(size, self.__init__, (1, 1))
        self.size = mgd_cast_type_dyn(size, gensym465, '175', gensym466)
        self.count = mgd_cast_type_dyn((((3 * size) * (size - 1)) + 1), gensym467, '176', gensym468)
        self.nodes_by_id = (cast12(self, gensym469, '177', gensym470).count * [None])
        self.nodes_by_pos = mgd_cast_type_dyn({}, gensym471, '178', gensym472)
        id = mgd_cast_type_dyn(0, gensym473, '179', gensym474)
        gensym492 = mgd_cast_type_function(xrange, gensym475, '180', gensym476)(size)
        for y in gensym492:
            gensym491 = mgd_cast_type_function(xrange, gensym477, '181', gensym478)((size + y))
            for x in gensym491:
                pos = (x, y)
                node = check13(Node(mgd_cast_type_dyn(pos, gensym479, '183', gensym480), id, mgd_cast_type_dyn([], gensym481, '183', gensym482)), Node, 2)
                cast14(self, gensym483, '184', gensym484).nodes_by_pos[pos] = mgd_cast_type_dyn(node, gensym485, '184', gensym486)
                cast15(self, gensym487, '185', gensym488).nodes_by_id[mgd_check_type_int(node.id, node, (0, 'id'))] = mgd_cast_type_dyn(node, gensym489, '185', gensym490)
                id = (id + 1)
        gensym510 = mgd_cast_type_function(xrange, gensym493, '187', gensym494)(1, size)
        for y in gensym510:
            gensym509 = mgd_cast_type_function(xrange, gensym495, '188', gensym496)(y, ((size * 2) - 1))
            for x in gensym509:
                ry = ((size + y) - 1)
                pos = (x, ry)
                node = check13(Node(mgd_cast_type_dyn(pos, gensym497, '191', gensym498), id, mgd_cast_type_dyn([], gensym499, '191', gensym500)), Node, 2)
                cast14(self, gensym501, '192', gensym502).nodes_by_pos[pos] = mgd_cast_type_dyn(node, gensym503, '192', gensym504)
                cast15(self, gensym505, '193', gensym506).nodes_by_id[mgd_check_type_int(node.id, node, (0, 'id'))] = mgd_cast_type_dyn(node, gensym507, '193', gensym508)
                id = (id + 1)

    def link_nodes(self):
        check16(self, self.link_nodes, (1, 0))
        gensym526 = mgd_check_type_list(self.nodes_by_id, self, (0, 'nodes_by_id'))
        for node in gensym526:
            check13(node, gensym526, 3)
            (x, y) = mgd_cast_type_tuple(node.pos, gensym519, '198', gensym520, 2)
            gensym525 = DIRS
            for dir in gensym525:
                check0(dir, gensym525, 3)
                nx = (x + mgd_check_type_int(dir.x, dir, (0, 'x')))
                ny = (y + mgd_check_type_int(dir.y, dir, (0, 'y')))
                if mgd_check_type_bool(mgd_check_type_function(self.contains_pos, self, (0, 'contains_pos'))(mgd_cast_type_tuple((nx, ny), gensym521, '202', gensym522, 2)), mgd_check_type_function(self.contains_pos, self, (0, 'contains_pos')), 2):
                    mgd_check_type_void(mgd_check_type_function(mgd_check_type_list(node.links, node, (0, 'links')).append, mgd_check_type_list(node.links, node, (0, 'links')), (0, 'append'))(mgd_check_type_int(check13(mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos'))[mgd_cast_type_tuple((nx, ny), gensym523, '203', gensym524, 2)], mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos')), 3).id, check13(mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos'))[mgd_cast_type_tuple((nx, ny), gensym523, '203', gensym524, 2)], mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos')), 3), (0, 'id'))), mgd_check_type_function(mgd_check_type_list(node.links, node, (0, 'links')).append, mgd_check_type_list(node.links, node, (0, 'links')), (0, 'append')), 2)

    def contains_pos(self, pos):
        check16(self, self.contains_pos, (1, 0))
        mgd_check_type_tuple(pos, self.contains_pos, (1, 1), 2)
        return (pos in mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos')))

    def get_by_pos(self, pos):
        check16(self, self.get_by_pos, (1, 0))
        mgd_check_type_tuple(pos, self.get_by_pos, (1, 1), 2)
        return check13(mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos'))[pos], mgd_check_type_dict(self.nodes_by_pos, self, (0, 'nodes_by_pos')), 3)

    def get_by_id(self, id):
        check16(self, self.get_by_id, (1, 0))
        mgd_check_type_int(id, self.get_by_id, (1, 1))
        return check13(mgd_check_type_list(self.nodes_by_id, self, (0, 'nodes_by_id'))[id], mgd_check_type_list(self.nodes_by_id, self, (0, 'nodes_by_id')), 3)
Hex = mgd_cast_type_class(Hex, gensym533, '171', gensym534, ['get_by_pos', 'contains_pos', 'link_nodes', '__init__', 'get_by_id'])


class Posn(retic_actual(object)):

    def __init__(self, hex, tiles, done=mgd_cast_type_dyn(None, gensym537, '218', gensym538)):
        self.hex = hex
        self.tiles = tiles
        self.done = (check1(Done(cast12(hex, gensym541, '221', gensym542).count), Done, 2) if (done is None) else done)

    def clone(self):
        return mgd_cast_type_function(Posn, gensym555, '224', gensym556)(cast3(self, gensym545, '224', gensym546).hex, cast17(self, gensym547, '224', gensym548).tiles, mgd_cast_type_function(cast19(cast18(self, gensym549, '224', gensym550).done, gensym551, '224', gensym552).clone, gensym553, '224', gensym554)())
Posn = Posn

def constraint_pass(pos, last_move=mgd_cast_type_dyn(None, gensym559, '227', gensym560)):
    changed = mgd_cast_type_dyn(False, gensym665, '228', gensym666)
    left = cast17(pos, gensym667, '229', gensym668).tiles[:]
    done = cast18(pos, gensym669, '230', gensym670).done
    free_cells = (mgd_cast_type_function(range, gensym673, '233', gensym674)(cast12(done, gensym671, '233', gensym672).count) if (last_move is None) else cast5(mgd_cast_type_function(cast4(cast3(pos, gensym675, '234', gensym676).hex, gensym677, '234', gensym678).get_by_id, gensym679, '234', gensym680)(last_move), gensym681, '234', gensym682).links)
    gensym713 = free_cells
    for i in gensym713:
        if (not mgd_cast_type_function(cast20(done, gensym683, '236', gensym684).already_done, gensym685, '236', gensym686)(i)):
            vmax = mgd_cast_type_dyn(0, gensym687, '237', gensym688)
            vmin = mgd_cast_type_dyn(0, gensym689, '238', gensym690)
            cells_around = cast5(mgd_cast_type_function(cast4(cast3(pos, gensym691, '239', gensym692).hex, gensym693, '239', gensym694).get_by_id, gensym695, '239', gensym696)(i), gensym697, '239', gensym698).links
            gensym703 = cells_around
            for nid in gensym703:
                if mgd_cast_type_function(cast20(done, gensym699, '241', gensym700).already_done, gensym701, '241', gensym702)(nid):
                    if (done[nid][0] != EMPTY):
                        vmin = (vmin + 1)
                        vmax = (vmax + 1)
                else:
                    vmax = (vmax + 1)
            gensym712 = mgd_cast_type_function(xrange, gensym704, '248', gensym705)(7)
            for num in gensym712:
                if ((num < vmin) or (num > vmax)):
                    if mgd_cast_type_function(cast21(done, gensym706, '250', gensym707).remove, gensym708, '250', gensym709)(i, num):
                        changed = mgd_cast_type_dyn(True, gensym710, '251', gensym711)
    gensym718 = cast22(done, gensym714, '254', gensym715).cells
    for cell in gensym718:
        if (mgd_cast_type_function(len, gensym716, '255', gensym717)(cell) == 1):
            left[cell[0]] = (left[cell[0]] - 1)
    gensym752 = mgd_cast_type_function(xrange, gensym719, '258', gensym720)(8)
    for v in gensym752:
        if ((cast17(pos, gensym721, '260', gensym722).tiles[v] > 0) and (left[v] == 0)):
            if mgd_cast_type_function(cast23(done, gensym723, '261', gensym724).remove_unfixed, gensym725, '261', gensym726)(v):
                changed = mgd_cast_type_dyn(True, gensym727, '262', gensym728)
        else:
            possible = mgd_cast_type_function(sum, gensym731, '264', gensym732)(((1 if (v in cell) else 0) for cell in cast22(done, gensym729, '264', gensym730).cells))
            if (cast17(pos, gensym733, '267', gensym734).tiles[v] == possible):
                gensym751 = mgd_cast_type_function(xrange, gensym737, '268', gensym738)(cast12(done, gensym735, '268', gensym736).count)
                for i in gensym751:
                    cell = cast22(done, gensym739, '269', gensym740).cells[i]
                    if ((not mgd_cast_type_function(cast20(done, gensym741, '270', gensym742).already_done, gensym743, '270', gensym744)(i)) and (v in cell)):
                        mgd_cast_type_function(cast24(done, gensym745, '271', gensym746).set_done, gensym747, '271', gensym748)(i, v)
                        changed = mgd_cast_type_dyn(True, gensym749, '272', gensym750)
    filled_cells = (mgd_cast_type_function(range, gensym755, '275', gensym756)(cast12(done, gensym753, '275', gensym754).count) if (last_move is None) else [last_move])
    gensym796 = filled_cells
    for i in gensym796:
        if mgd_cast_type_function(cast20(done, gensym757, '278', gensym758).already_done, gensym759, '278', gensym760)(i):
            num = done[i][0]
            empties = mgd_cast_type_dyn(0, gensym761, '280', gensym762)
            filled = mgd_cast_type_dyn(0, gensym763, '281', gensym764)
            unknown = []
            cells_around = cast5(mgd_cast_type_function(cast4(cast3(pos, gensym765, '283', gensym766).hex, gensym767, '283', gensym768).get_by_id, gensym769, '283', gensym770)(i), gensym771, '283', gensym772).links
            gensym777 = cells_around
            for nid in gensym777:
                if mgd_cast_type_function(cast20(done, gensym773, '285', gensym774).already_done, gensym775, '285', gensym776)(nid):
                    if (done[nid][0] == EMPTY):
                        empties = (empties + 1)
                    else:
                        filled = (filled + 1)
                else:
                    mgd_check_type_void(mgd_check_type_function(unknown.append, unknown, (0, 'append'))(nid), mgd_check_type_function(unknown.append, unknown, (0, 'append')), 2)
            if (mgd_cast_type_function(len, gensym778, '292', gensym779)(unknown) > 0):
                if (num == filled):
                    gensym786 = unknown
                    for u in gensym786:
                        if (EMPTY in done[u]):
                            mgd_cast_type_function(cast24(done, gensym780, '296', gensym781).set_done, gensym782, '296', gensym783)(u, EMPTY)
                            changed = mgd_cast_type_dyn(True, gensym784, '297', gensym785)
                elif (num == (filled + mgd_cast_type_function(len, gensym787, '300', gensym788)(unknown))):
                    gensym795 = unknown
                    for u in gensym795:
                        if mgd_cast_type_function(cast21(done, gensym789, '302', gensym790).remove, gensym791, '302', gensym792)(u, EMPTY):
                            changed = mgd_cast_type_dyn(True, gensym793, '303', gensym794)
    return mgd_cast_type_bool(changed, gensym797, '305', gensym798)
ASCENDING = 1
DESCENDING = (- 1)

def find_moves(pos, strategy, order):
    mgd_check_type_int(strategy, find_moves, (1, 1))
    mgd_check_type_int(order, find_moves, (1, 2))
    done = cast18(pos, gensym825, '311', gensym826).done
    cell_id = mgd_cast_type_function(cast25(done, gensym827, '312', gensym828).next_cell, gensym829, '312', gensym830)(pos, strategy)
    if (cell_id < 0):
        return mgd_cast_type_dyn([], gensym831, '314', gensym832)
    if (order == ASCENDING):
        return mgd_cast_type_dyn(mgd_cast_type_list([(cell_id, v) for v in done[cell_id]], gensym833, '317', gensym834), gensym835, '317', gensym836)
    else:
        moves = mgd_cast_type_function(list, gensym841, '320', gensym842)(mgd_cast_type_function(reversed, gensym839, '320', gensym840)(mgd_cast_type_list([(cell_id, v) for v in done[cell_id] if (v != EMPTY)], gensym837, '320', gensym838)))
        if (EMPTY in done[cell_id]):
            mgd_cast_type_function(cast26(moves, gensym843, '322', gensym844).append, gensym845, '322', gensym846)((cell_id, EMPTY))
        return moves

def play_move(pos, move):
    mgd_check_type_tuple(move, play_move, (1, 1), 2)
    (cell_id, i) = move
    mgd_cast_type_function(cast24(cast18(pos, gensym849, '327', gensym850).done, gensym851, '327', gensym852).set_done, gensym853, '327', gensym854)(cell_id, i)

def print_pos(pos, output):
    hex = cast3(pos, gensym933, '330', gensym934).hex
    done = cast18(pos, gensym935, '331', gensym936).done
    size = cast27(hex, gensym937, '332', gensym938).size
    gensym970 = mgd_cast_type_function(xrange, gensym939, '333', gensym940)(size)
    for y in gensym970:
        mgd_cast_type_function(print, gensym943, '334', gensym944)((u_lit(mgd_cast_type_dyn(' ', gensym941, '334', gensym942)) * ((size - y) - 1)), end=u_lit(''), file=output)
        gensym967 = mgd_cast_type_function(xrange, gensym945, '335', gensym946)((size + y))
        for x in gensym967:
            pos2 = (x, y)
            id = cast29(mgd_cast_type_function(cast28(hex, gensym947, '337', gensym948).get_by_pos, gensym949, '337', gensym950)(pos2), gensym951, '337', gensym952).id
            if mgd_cast_type_function(cast20(done, gensym953, '338', gensym954).already_done, gensym955, '338', gensym956)(id):
                c = (mgd_cast_type_function(unicode, gensym957, '339', gensym958)(done[id][0]) if (done[id][0] != EMPTY) else u_lit(mgd_cast_type_dyn('.', gensym959, '339', gensym960)))
            else:
                c = u_lit(mgd_cast_type_dyn('?', gensym961, '341', gensym962))
            mgd_cast_type_function(print, gensym965, '342', gensym966)((u_lit(mgd_cast_type_dyn('%s ', gensym963, '342', gensym964)) % c), end=u_lit(''), file=output)
        mgd_cast_type_function(print, gensym968, '343', gensym969)(end=u_lit('\n'), file=output)
    gensym1002 = mgd_cast_type_function(xrange, gensym971, '344', gensym972)(1, size)
    for y in gensym1002:
        mgd_cast_type_function(print, gensym975, '345', gensym976)((u_lit(mgd_cast_type_dyn(' ', gensym973, '345', gensym974)) * y), end=u_lit(''), file=output)
        gensym999 = mgd_cast_type_function(xrange, gensym977, '346', gensym978)(y, ((size * 2) - 1))
        for x in gensym999:
            ry = ((size + y) - 1)
            pos2 = (x, ry)
            id = cast29(mgd_cast_type_function(cast28(hex, gensym979, '349', gensym980).get_by_pos, gensym981, '349', gensym982)(pos2), gensym983, '349', gensym984).id
            if mgd_cast_type_function(cast20(done, gensym985, '350', gensym986).already_done, gensym987, '350', gensym988)(id):
                c = (mgd_cast_type_function(unicode, gensym989, '351', gensym990)(done[id][0]) if (done[id][0] != EMPTY) else u_lit(mgd_cast_type_dyn('.', gensym991, '351', gensym992)))
            else:
                c = u_lit(mgd_cast_type_dyn('?', gensym993, '353', gensym994))
            mgd_cast_type_function(print, gensym997, '354', gensym998)((u_lit(mgd_cast_type_dyn('%s ', gensym995, '354', gensym996)) % c), end=u_lit(''), file=output)
        mgd_cast_type_function(print, gensym1000, '355', gensym1001)(end=u_lit('\n'), file=output)
OPEN = 0
SOLVED = 1
IMPOSSIBLE = (- 1)

def solved(pos, output, verbose=mgd_cast_type_dyn(False, gensym1005, '361', gensym1006)):
    hex = cast3(pos, gensym1039, '362', gensym1040).hex
    tiles = cast17(pos, gensym1041, '363', gensym1042).tiles[:]
    done = cast18(pos, gensym1043, '364', gensym1044).done
    exact = mgd_cast_type_dyn(True, gensym1045, '365', gensym1046)
    all_done = mgd_cast_type_dyn(True, gensym1047, '366', gensym1048)
    gensym1078 = mgd_cast_type_function(xrange, gensym1051, '367', gensym1052)(cast12(hex, gensym1049, '367', gensym1050).count)
    for i in gensym1078:
        if (mgd_cast_type_function(len, gensym1053, '368', gensym1054)(done[i]) == 0):
            return IMPOSSIBLE
        elif mgd_cast_type_function(cast20(done, gensym1055, '370', gensym1056).already_done, gensym1057, '370', gensym1058)(i):
            num = done[i][0]
            tiles[num] = (tiles[num] - 1)
            if (tiles[num] < 0):
                return IMPOSSIBLE
            vmax = mgd_cast_type_dyn(0, gensym1059, '375', gensym1060)
            vmin = mgd_cast_type_dyn(0, gensym1061, '376', gensym1062)
            if (num != EMPTY):
                cells_around = cast5(mgd_cast_type_function(cast4(hex, gensym1063, '378', gensym1064).get_by_id, gensym1065, '378', gensym1066)(i), gensym1067, '378', gensym1068).links
                gensym1073 = cells_around
                for nid in gensym1073:
                    if mgd_cast_type_function(cast20(done, gensym1069, '380', gensym1070).already_done, gensym1071, '380', gensym1072)(nid):
                        if (done[nid][0] != EMPTY):
                            vmin = (vmin + 1)
                            vmax = (vmax + 1)
                    else:
                        vmax = (vmax + 1)
                if ((num < vmin) or (num > vmax)):
                    return IMPOSSIBLE
                if (num != vmin):
                    exact = mgd_cast_type_dyn(False, gensym1074, '390', gensym1075)
        else:
            all_done = mgd_cast_type_dyn(False, gensym1076, '392', gensym1077)
    if ((not all_done) or (not exact)):
        return OPEN
    print_pos(pos, output)
    return SOLVED

def solve_step(prev, strategy, order, output, first=mgd_cast_type_dyn(False, gensym1081, '400', gensym1082)):
    if first:
        pos = mgd_cast_type_function(cast19(prev, gensym1107, '402', gensym1108).clone, gensym1109, '402', gensym1110)()
        while mgd_check_type_bool(constraint_pass(pos), constraint_pass, 2):
            pass
    else:
        pos = prev
    moves = find_moves(pos, mgd_cast_type_int(strategy, gensym1111, '408', gensym1112), mgd_cast_type_int(order, gensym1113, '408', gensym1114))
    if (mgd_cast_type_function(len, gensym1115, '409', gensym1116)(moves) == 0):
        return mgd_check_type_int(solved(pos, output), solved, 2)
    else:
        gensym1129 = moves
        for move in gensym1129:
            ret = mgd_cast_type_dyn(OPEN, gensym1117, '414', gensym1118)
            new_pos = mgd_cast_type_function(cast19(pos, gensym1119, '415', gensym1120).clone, gensym1121, '415', gensym1122)()
            play_move(new_pos, mgd_cast_type_tuple(move, gensym1123, '416', gensym1124, 2))
            while mgd_check_type_bool(constraint_pass(new_pos, move[0]), constraint_pass, 2):
                pass
            cur_status = mgd_check_type_int(solved(new_pos, output), solved, 2)
            if (cur_status != OPEN):
                ret = mgd_cast_type_dyn(cur_status, gensym1125, '422', gensym1126)
            else:
                ret = mgd_cast_type_dyn(mgd_check_type_int(solve_step(new_pos, strategy, order, output), solve_step, 2), gensym1127, '424', gensym1128)
            if (ret == SOLVED):
                return SOLVED
    return IMPOSSIBLE

def check_valid(pos):
    hex = cast3(pos, gensym1148, '430', gensym1149).hex
    tiles = cast17(pos, gensym1150, '431', gensym1151).tiles
    done = cast18(pos, gensym1152, '432', gensym1153).done
    tot = mgd_cast_type_dyn(0, gensym1154, '434', gensym1155)
    gensym1160 = mgd_cast_type_function(xrange, gensym1156, '435', gensym1157)(8)
    for i in gensym1160:
        if (tiles[i] > 0):
            tot = (tot + tiles[i])
        else:
            tiles[i] = mgd_cast_type_dyn(0, gensym1158, '439', gensym1159)
    if (tot != cast12(hex, gensym1161, '441', gensym1162).count):
        raise mgd_cast_type_function(Exception, gensym1165, '442', gensym1166)(('Invalid input. Expected %d tiles, got %d.' % (cast12(hex, gensym1163, '442', gensym1164).count, tot)))

def solve(pos, strategy, order, output):
    mgd_check_type_int(strategy, solve, (1, 1))
    mgd_check_type_int(order, solve, (1, 2))
    check_valid(pos)
    return mgd_check_type_int(solve_step(pos, mgd_cast_type_dyn(strategy, gensym1169, '446', gensym1170), mgd_cast_type_dyn(order, gensym1171, '446', gensym1172), output, first=True), solve_step, 2)

def read_file(file):
    lines = mgd_cast_type_list([mgd_cast_type_function(cast31(line, gensym1287, '452', gensym1288).strip, gensym1289, '452', gensym1290)('\r\n') for line in mgd_cast_type_function(cast30(file, gensym1283, '452', gensym1284).splitlines, gensym1285, '452', gensym1286)()], gensym1291, '452', gensym1292)
    size = mgd_cast_type_function(int, gensym1293, '453', gensym1294)(lines[0])
    hex = cast32(check16(Hex(mgd_cast_type_int(size, gensym1295, '454', gensym1296)), Hex, 2), gensym1297, '454', gensym1298)
    linei = mgd_cast_type_dyn(1, gensym1299, '455', gensym1300)
    tiles = (8 * [0])
    done = cast2(check1(Done(mgd_cast_type_dyn(mgd_check_type_int(hex.count, hex, (0, 'count')), gensym1301, '457', gensym1302)), Done, 2), gensym1303, '457', gensym1304)
    gensym1330 = mgd_cast_type_function(xrange, gensym1305, '458', gensym1306)(size)
    for y in gensym1330:
        line = lines[mgd_cast_type_int(linei, gensym1307, '459', gensym1308)][((size - y) - 1):]
        p = mgd_cast_type_dyn(0, gensym1309, '460', gensym1310)
        gensym1329 = mgd_cast_type_function(xrange, gensym1311, '461', gensym1312)((size + y))
        for x in gensym1329:
            tile = line[p:(p + 2)]
            p = (p + 2)
            if (tile[1] == '.'):
                inctile = mgd_cast_type_dyn(EMPTY, gensym1313, '465', gensym1314)
            else:
                inctile = mgd_cast_type_function(int, gensym1315, '467', gensym1316)(tile)
            tiles[mgd_cast_type_int(inctile, gensym1319, '468', gensym1320)] = (mgd_check_type_int(tiles[mgd_cast_type_int(inctile, gensym1317, '468', gensym1318)], tiles, 3) + 1)
            if (tile[0] == '+'):
                mgd_cast_type_function(print, gensym1323, '471', gensym1324)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, y, mgd_check_type_int(check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, y), gensym1321, '472', gensym1322, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2).id, check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, y), gensym1321, '472', gensym1322, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2), (0, 'id')))))
                mgd_check_type_function(done.set_done, done, (0, 'set_done'))(mgd_check_type_int(check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, y), gensym1325, '473', gensym1326, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2).id, check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, y), gensym1325, '473', gensym1326, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2), (0, 'id')), mgd_cast_type_int(inctile, gensym1327, '473', gensym1328))
        linei = (linei + 1)
    gensym1356 = mgd_cast_type_function(xrange, gensym1331, '476', gensym1332)(1, size)
    for y in gensym1356:
        ry = ((size - 1) + y)
        line = lines[mgd_cast_type_int(linei, gensym1333, '478', gensym1334)][y:]
        p = mgd_cast_type_dyn(0, gensym1335, '479', gensym1336)
        gensym1355 = mgd_cast_type_function(xrange, gensym1337, '480', gensym1338)(y, ((size * 2) - 1))
        for x in gensym1355:
            tile = line[p:(p + 2)]
            p = (p + 2)
            if (tile[1] == '.'):
                inctile = mgd_cast_type_dyn(EMPTY, gensym1339, '484', gensym1340)
            else:
                inctile = mgd_cast_type_function(int, gensym1341, '486', gensym1342)(tile)
            tiles[mgd_cast_type_int(inctile, gensym1345, '487', gensym1346)] = (mgd_check_type_int(tiles[mgd_cast_type_int(inctile, gensym1343, '487', gensym1344)], tiles, 3) + 1)
            if (tile[0] == '+'):
                mgd_cast_type_function(print, gensym1349, '490', gensym1350)(('Adding locked tile: %d at pos %d, %d, id=%d' % (inctile, x, ry, mgd_check_type_int(check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, ry), gensym1347, '491', gensym1348, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2).id, check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, ry), gensym1347, '491', gensym1348, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2), (0, 'id')))))
                mgd_check_type_function(done.set_done, done, (0, 'set_done'))(mgd_check_type_int(check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, ry), gensym1351, '492', gensym1352, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2).id, check13(mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos'))(mgd_cast_type_tuple((x, ry), gensym1351, '492', gensym1352, 2)), mgd_check_type_function(hex.get_by_pos, hex, (0, 'get_by_pos')), 2), (0, 'id')), mgd_cast_type_int(inctile, gensym1353, '492', gensym1354))
        linei = (linei + 1)
    mgd_check_type_function(hex.link_nodes, hex, (0, 'link_nodes'))()
    mgd_check_type_function(done.filter_tiles, done, (0, 'filter_tiles'))(tiles)
    return mgd_cast_type_function(Posn, gensym1357, '496', gensym1358)(hex, tiles, done)

def solve_file(file, strategy, order, output):
    mgd_check_type_int(strategy, solve_file, (1, 1))
    mgd_check_type_int(order, solve_file, (1, 2))
    pos = read_file(file)
    mgd_check_type_int(solve(pos, strategy, order, output), solve, 2)

def run_level36():
    f = '4\n    2 1 1 2\n   3 3 3 . .\n  2 3 3 . 4 .\n . 2 . 2 4 3 2\n  2 2 . . . 2\n   4 3 4 . .\n    3 2 3 3\n'
    order = DESCENDING
    strategy = Done.FIRST_STRATEGY
    output = mgd_cast_type_function(StringIO, gensym1367, '515', gensym1368)()
    solve_file(mgd_cast_type_dyn(f, gensym1369, '516', gensym1370), mgd_cast_type_int(strategy, gensym1371, '516', gensym1372), order, output)
    expected = '   3 4 3 2 \n  3 4 4 . 3 \n 2 . . 3 4 3 \n2 . 1 . 3 . 2 \n 3 3 . 2 . 2 \n  3 . 2 . 2 \n   2 2 . 1 \n'
    if (mgd_cast_type_function(cast33(output, gensym1373, '526', gensym1374).getvalue, gensym1375, '526', gensym1376)() != expected):
        raise mgd_cast_type_function(AssertionError, gensym1381, '527', gensym1382)(('got a wrong answer:\n%s' % mgd_cast_type_function(cast33(output, gensym1377, '527', gensym1378).getvalue, gensym1379, '527', gensym1380)()))

def main(n, timer):
    l = []
    gensym1403 = mgd_cast_type_function(xrange, gensym1397, '533', gensym1398)(n)
    for i in gensym1403:
        t0 = mgd_cast_type_function(timer, gensym1399, '534', gensym1400)()
        run_level36()
        time_elapsed = (mgd_cast_type_function(timer, gensym1401, '536', gensym1402)() - t0)
        mgd_check_type_void(mgd_check_type_function(l.append, l, (0, 'append'))(time_elapsed), mgd_check_type_function(l.append, l, (0, 'append')), 2)
        blame_set.clear()
    return mgd_cast_type_dyn(l, gensym1404, '538', gensym1405)
if (__name__ == '__main__'):
    import util, optparse
    parser = mgd_cast_type_function(cast34(optparse, gensym1406, '542', gensym1407).OptionParser, gensym1408, '542', gensym1409)(usage='%prog [options]', description='Test the performance of the hexiom2 benchmark')
    mgd_check_type_function(util.add_standard_options_to, util, (0, 'add_standard_options_to'))(parser)
    (options, args) = mgd_cast_type_tuple(mgd_cast_type_function(cast35(parser, gensym1410, '546', gensym1411).parse_args, gensym1412, '546', gensym1413)(), gensym1414, '546', gensym1415, 2)
    mgd_check_type_function(util.run_benchmark, util, (0, 'run_benchmark'))(options, mgd_cast_type_dyn(10, gensym1416, '548', gensym1417), mgd_cast_type_dyn(main, gensym1418, '548', gensym1419))
