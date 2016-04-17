(* Homework 1 *)

(* fn : (int * int * int ) * (int * int * int) -> bool *)
fun is_older (date1 : (int * int * int), date2 : (int * int * int)) =
  if #1 date1 < #1 date2
  then true
  else if #1 date1 > #1 date2 
  then false
  else if #2 date1 <  #2 date2
  then true
  else if #2 date1 > #2 date2
  then false
  else if #3 date1 < #3 date2
  then true
  else false

(* -> int *)
fun number_in_month (dates : (int * int * int) list, m : int) =
  let 
      fun is_mount(date : (int * int * int), m: int) =  #2 date = m
  in
      if null dates 
      then 0
      else if is_mount( (hd dates), m)
      then 1 + number_in_month(tl dates, m)
      else 0 + number_in_month(tl dates, m)
  end

(* -> int *)
fun number_in_months (dates : (int * int * int) list, ms: int list) =
  if null ms
  then 0
  else number_in_month(dates, hd ms) + number_in_months(dates, tl ms)

(* -> (int*int*int) list *)
fun dates_in_month (dates : (int * int * int) list, m : int) =
  let 
      fun get_day (date: (int * int * int), m : int) = 
	if #2 date <> m 
	then NONE
	else SOME( date )
  in
      if null dates 
      then []
      else 
	  let 
	      val valofdate = get_day(hd(dates),m)
	  in 
	      if isSome(valofdate)
	      then valOf(valofdate) :: dates_in_month(tl(dates), m)
	      else dates_in_month(tl(dates), m)
	  end
  end

(* APPEND fun append (lst1: a list, lst2: a list) *)


(* dates in months -> (int * int * int) list *)

fun dates_in_months(dates : (int * int * int) list, months: int list) = 
  if null months 
  then []
  else dates_in_month(dates, hd(months)) @ dates_in_months(dates, tl(months)) (* @?? *)

(* -> string *)
fun date_to_string(date : (int * int * int)) =
  let
      fun int_to_months(m:int) = 
	let
	    val months = ["January", "February", "March", "April", "May", "June",
			  "June", "July", "August", "September", "October", "November",
			  "December"]
	in 
	    List.nth(months, m-1)
	end
  in
      int_to_months(#2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
  end
      
(* 8. -> int *)
fun number_before_reaching_sum (sum : int, ns : int list) = 
  let fun count (sum : int, cnt : int) = 
	if sum > 0 
	then count(sum - List.nth(ns, cnt), cnt + 1)
	else cnt - 1
  in
      count(sum, 0)
  end

(*#9. -> int *)
fun what_month( days : int) = 
  let 
      val months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  in
      number_before_reaching_sum(days, months) + 1
  end

(* #10. -> int list *)

fun enumeratex(n1: int, n2: int) = 
  if n1 = n2 
  then [n2]
  else
      n1 :: enumeratex(n1+1, n2)

fun month_range(day1 : int, day2 : int) = 
  let 
      val mon1 = what_month(day1)
      val mon2 = what_month(day2)
  in
      if day1 > day2 
      then []
      else enumeratex(mon1, mon2)
  end

(* #11 -> (int * int * int) option *)
fun oldest ( dates: (int * int * int) list ) = 
  let 
      fun max_date ( dates : (int * int * int) list ) = 
	(* a map function will be really appreciated10 here *)
	if null (tl dates)
	then hd dates
	else 
	    let val other = max_date(tl dates)
	    in 
		if is_older(hd(dates), other)
		then hd(dates)
		else other
	    end
  in
      if null dates
      then NONE
      else SOME ( max_date(dates) )
  end

(* Remove duplicate in a list *) 
fun ele_exist(ns: int list, target : int) = 
  if null ns 
  then false
  else if hd ns = target
  then true
  else ele_exist(tl ns, target)

fun remove_duplicate ( ns : int list ) = 
  let 
      fun filterx (head : int list, tail : int list) = 
	if null tail 
	then rev head
	else if ele_exist(head, (hd tail))
	then filterx(head, tl tail)
	else filterx((hd tail) :: head, tl tail)
  in
      filterx([], ns)
  end

(* Test *)

val date1 = (2008, 3, 5);
val date2 = (2013, 4, 14);
val date3 = (2008, 3, 6);

is_older(date1, date2) = true;
number_in_month([date1, date2, date3], 3) = 2;
number_in_month([], 4) = 0;
number_in_months([date1, date2, date3], [3, 4, 5]) = 3;
dates_in_month([date1, date2, date3], 3) = [date1, date3];
dates_in_months([date1, date2, date3], [3,4]) = [date1, date3, date2]
date_to_string(date1) = "March 5, 2008";
number_before_reaching_sum(5  ,[1, 4, 12, 3]) = 1;
number_before_reaching_sum(10 ,[1, 4, 12, 3]) = 2;
number_before_reaching_sum(17 ,[1, 4, 12, 3]) = 2;
what_month(31) = 1;
what_month(32) = 2;
enumeratex(1, 5) = [1,2,3,4,5];
month_range(31, 32) = [1, 2];
month_range(1, 365) = [1,2,3,4,5,6,7,8,9,10,11,12];
valOf(oldest([date1, date2, date3])) = date1;
remove_duplicate([1,2,3,1,2,2,2,2,2,2,3,5,4]) = [1,2,3,5,4];
