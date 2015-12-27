(* Dan Grossman, CSE341 Spring 2013, HW3 Provided Code *)

(* 1-6 *)

fun only_capitals strs = 
  List.filter (fn s => Char.isUpper(String.sub (s, 0))) strs

fun longest_string1 strs = 
  List.foldl (fn (s1,s2) => if String.size s1 > String.size s2 then s1 else s2) "" strs

fun longest_string2 strs = 
  List.foldl (fn (s1, s2) => if String.size s1 >= String.size s2 then s1 else s2) "" strs

fun longest_string_helper f strs = 
  List.foldl (fn (s1, s2) => if f(String.size s1, String.size s2) then s1 else s2) "" strs

val longest_string3 = longest_string_helper (fn (i,j) => i > j)
val longest_string4 = longest_string_helper (fn (i,j) => i >= j)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = implode o rev o explode


val StringList = ["Ha", "haha", "Hahaha", "wuhaha"];
only_capitals StringList = ["Ha", "Hahaha"];
longest_string1 StringList = "Hahaha";
longest_string2 StringList = "wuhaha";
longest_string3 StringList = "Hahaha";
longest_string4 StringList = "wuhaha";
longest_capitalized StringList = "Hahaha";
rev_string "Fuck" = "kcuF";

(* 7-8 *)
exception NoAnswer

(* ('a -> 'b option) -> 'a list -> 'b *)
fun first_answer f lst =
  case lst of 
      [] => raise NoAnswer
    | x::xs => 
      case f x of 
	  SOME v => v
	| NONE => first_answer f xs
(* ('a -> 'b list option) -> 'a list -> 'b list option *)
fun all_answers f list =
  let fun accumulate(xs, acc) = 
	case xs of
	    [] => SOME acc
	  | x::xs' => 
	    case f x of 
		NONE => NONE
	      | SOME v => accumulate(xs', v @ acc)
  in
      accumulate(list, [])
  end

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(* 9 *)
val count_wildcards = g (fn () => 1) (fn _ => 0)
val count_wild_and_variable_lengths = g (fn () => 1) String.size 
fun count_some_var (s, p) =
  g (fn () => 0) (fn x => if x = s then 1 else 0) p 

(* 10 *)
fun check_repeat strs = 
  case strs of 
      [] => false
    | x::xs => if List.exists (fn c => (c = x)) xs
	      then false
	      else check_repeat xs

fun list_strings pat = 
  case pat of 
      Variable s => s::[]
    | TupleP ps => List.foldl (fn (p, s) => (list_strings p) @ s) [] ps
    | ConstructorP (_, pat) => list_strings pat
    | _ => []

fun check_pat pat = check_repeat(list_strings pat)
      
(* 11 12 -- UNFINISHED!!!*)

(* -> (string * value) list option *)

(* fun match (v, pat) = 
  case (v, pat) of 
      (_, Wilcard) => SOME []
    | (v, Variable s) => SOME (s, v)::[]
    | (Unit, UnitP) => SOME []
    | (Const _, ConstP _) => SOME []
    | (Tuple vs, TupleP ps) => 
      all_answers(match, ListPair.zip (v, pat))
    | (Constructor(s2,v), ConstructorP(s1,p))
      => if s1=s2 then match(v, p) else NONE
    | _ => NONE *)
 

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)
