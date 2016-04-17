(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)

(* 1 : assume the string is in the list at most once *)
fun all_except_option (str, strs) = 
  case strs of 
      [] => NONE
    | x :: xs =>
      case same_string(x, str) of
	  true => SOME xs
	| false => 
	  case all_except_option(str, xs) of 
	      NONE => NONE
	    | SOME y => SOME (x::y)

(* 2 : Assume no repeat*)
fun get_substitutions1 (name, nameslist) = 
  case nameslist of 
      [] => []
    | nlist :: nss => 
      case all_except_option(name, nlist) of 
	  NONE => get_substitutions1 (name, nss)
	| SOME y => y @ get_substitutions1 (name, nss)

(* 3 *)
fun get_substitutions2 (name, nameslist) = 
  let 
      fun find_sub (nameslist, currentnames) = 
	case nameslist of 
	    [] => currentnames
	  | nlist :: nss => 
	    case all_except_option(name, nlist) of
		NONE => find_sub(nss, currentnames)
	      | SOME y => find_sub(nss, y @ currentnames)
  in
      find_sub(nameslist, [])
  end

(* 4 *) 
fun similar_names (nameslist, {first=x, middle=y, last=z}) = 
  let 
      val sublist = get_substitutions2(x, nameslist)
      fun replace(namelist) = 
	case namelist of 
	    [] => []
	  | n::ns =>
	    {first=n, middle=y, last=z} :: replace(ns)
  in
      replace(x::sublist)
  end

(* TEST of SET 1 *)
val str1 = "Fred";
val str2 = "Sam";
val str3 = "Jon";
val namelists =  [["Fred", "Fredrick"], ["Elizabeth", "Betty"], ["Freddie", "Fred", "F"]];
all_except_option(str1, [str2, str2, str2]) = NONE;
all_except_option(str1, [str3, str1, str2]) = SOME [str3, str2];
get_substitutions1("Fred", namelists) = ["Fredrick", "Freddie", "F"];
get_substitutions2("Fred", namelists) = ["Freddie", "F", "Fredrick"];
similar_names(namelists, {first="Fred", middle="D", last="Stark"}) = 
 [{first="Fred",last="Stark",middle="D"},
  {first="Freddie",last="Stark",middle="D"},
  {first="F",last="Stark",middle="D"},
  {first="Fredrick",last="Stark",middle="D"}];

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color ( (s, _) : card) = 
  case s of 
      Clubs => Black
   | Spades => Black
   | _  => Red

fun card_value ( (_, r) : card) = 
  case r of 
      Num i => i
   | Ace => 11
   | _ => 10

fun remove_card (cs, c, e) = 
  case cs of 
      [] => raise e
    | x :: xs => 
      if x = c then xs else x :: remove_card(xs, c, e)

fun all_same_color (cs) = 
  case cs of 
      [] => true
    | x::[] => true
    | head::(neck::rest) => 
      (card_color(head) = card_color(neck) 
       andalso all_same_color(neck::rest))

fun sum_cards (cs) = 
  let fun sumx (cs, acc) = 
	case cs of 
	    [] => acc
	  | x::xs => sumx(xs, acc + card_value(x))
  in
      sumx(cs, 0)
  end

fun score (hand, goal) = 
  let 
      fun abs (a) = if a >= 0 then a else ~a
      val foo = sum_cards(hand) - goal
      val hscore = abs(foo);
      val isLarger = foo > 0
      val isSameSuit = all_same_color(hand)
  in
      case (isSameSuit, isLarger) of 
	  (false, false) => hscore
       | (false, true) => 3 * hscore
       | (true, false)  => hscore div 2
       | _  => 3 * hscore div 2
  end

fun officiate (cards, moves, goal) =
  let
      fun run_game (hand, cards, moves) = 
	case (cards, moves) of 
	    ([], _) => hand
	 | (_, []) => hand
	 | (c::cs, m::ms) => 
	   case m of 
	       Discard c => 
	       run_game(remove_card(hand, c, IllegalMove), c::cs, ms)
	     | _ => if sum_cards(c::hand) > goal 
		    then hand 
		    else run_game(c::hand, cs, ms)
      val hands = run_game([], cards, moves)
  in
      score(hands, goal)
  end

val card1 = (Clubs, Num(9));
val card2 = (Hearts, King);
val card3 = (Diamonds, Jack);
val card4 = (Spades, Num(4));

card_color(card1) = Black;
card_value(card2) = 10;
remove_card([card3, card2, card1], card2, IllegalMove) = [card3, card1];
(* remove_card([card3, card1], card2, IllegalMove); *) 
all_same_color([card1, card1, card1]) = true;
all_same_color([card1, card2]) = false;
sum_cards([card1, card2, card3]) = 29;
score([card1, card2, card3], 13) = 48;
score([card2, card2, card2], 13) = 25;
score([card4, card4, card4], 13) = 0;

(* The result 60 doesn't seem right *)
officiate([card1, card2, card3, card4], [Draw, Draw, Draw, Draw, Discard(card4)], 13);
		     
