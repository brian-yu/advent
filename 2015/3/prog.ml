#use "topfind"
#require "base"
(* #require "core" *)
#require "stdio"
open Base
(* open Core  *)
open Stdio

type coord = {x: int, y: int};;

let solve i s = 
  match String.get s i with
  | '>' -> 
;;

let read_file filename solve = 
  let file = In_channel.create filename in
  let lines = match (In_channel.input_line) with
    | Some line -> line
    | None -> ""
  printf "%d\n" (solve lines)
;;

read_file "input.txt" (solve) ;;
