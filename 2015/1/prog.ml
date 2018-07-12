#use "topfind"
#require "base"
#require "stdio"
open Base 
open Stdio

let solve text = 
  let lefts = String.filter text (fun c -> phys_equal c '(') in
  let rights = String.filter text (fun c -> phys_equal c ')') in
  String.length lefts - String.length rights
;;

let rec solve2 floor index text =
  let len = ((String.length text) - 1) in
  if floor = -1 then index
  else if index = len then floor
  else match (String.get text index) with
    | '(' -> solve2 (floor + 1) (index + 1) text
    | ')' -> solve2 (floor - 1) (index + 1) text
    | _ -> solve2 floor (index + 1) text
;;

let read_file filename solve = 
  let file = In_channel.create filename in
  let text = 
    match In_channel.input_line file with
    | Some x -> x
    | None -> ""
  in
  printf "%d\n" (solve text)
;;

read_file "input.txt" (solve2 0 0)
