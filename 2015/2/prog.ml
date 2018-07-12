#use "topfind"
#require "base"
(* #require "core" *)
#require "stdio"
open Base
(* open Core  *)
open Stdio

let dims line = List.map (
    String.split line 'x'
  ) ~f: (fun x -> int_of_string x)
;;
let sides x = match x with
  | l::w::h::[] -> [l*w; w*h; h*l]
  | _ -> []
;;
let smallest x = match (List.reduce ~f:(fun acc elt ->
    if elt < acc then elt
    else acc
  ) x) with
  | Some elt -> elt
  | None -> 0
;;
let solve lines = 
  let area x = (List.fold ~init:0 ~f:(fun acc elt ->
      acc + 2*elt
    ) x) + (smallest x) in
  match (List.reduce ~f:(+) (List.map ~f:(fun line -> (area (sides (dims line)))) lines)) with
  | Some res -> res
  | None -> 0
;;

let ribbon lines = 
  let len x = match (List.sort (fun a b -> a - b) x) with
    | fst::snd::trd::[] -> 2*fst + 2*snd + fst*snd*trd
    | _ -> 0 in
  match (List.reduce ~f:(+) (List.map ~f:(fun line -> len (dims line)) lines)) with
  | Some x -> x
  | None -> 0
;;

let read_file filename solve = 
  let file = In_channel.create filename in
  let lines = In_channel.input_lines file in
  printf "%d\n" (solve lines)
;;

read_file "input.txt" (solve) ;;
read_file "input.txt" (ribbon) ;;
