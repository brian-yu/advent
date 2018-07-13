#use "topfind"
#require "base"
#require "stdio"
open Base
open Stdio

module Coord = struct
  module T = struct

    type t = { x: int; y: int}

    let compare a b =
      match a.x - b.x with
      | 0 -> a.y - b.y
      | _ -> a.x - b.x

    let sexp_of_t t : Sexp.t =
      List [ Atom (Int.to_string t.x); Atom (Int.to_string t.y) ]
    ;;
  end
  include T;;
  include Comparator.Make(T);;
end;;

include Coord;;

let rec visited (i : int) (s : string) (l : Coord.T.t list) = 
  if i = (String.length s) - 1 then l
  else let c = match List.last l  with
      | Some x -> x
      | None -> {x=0; y=0} in
  match String.get s i with
    | '>' -> visited (i+1) s (List.append l [{x=(c.x+1); y = c.y}])
    | '<' -> visited (i+1) s (List.append l [{x=(c.x-1); y = c.y}])
    | '^' -> visited (i+1) s (List.append l [{x=c.x; y = (c.y+1)}])
    | 'v' -> visited (i+1) s (List.append l [{x=c.x; y = (c.y-1)}])
    | _ -> l
;;

let solve l =
  Set.length (Set.of_list (module Coord) (visited 0 l [{x=0;y=0}]))
;;

let read_file filename solve = 
  let file = In_channel.create filename in
  let lines = match (In_channel.input_line file) with
    | Some line -> line
    | None -> "" in
  printf "%d\n" (solve lines)
;;

read_file "input.txt" solve ;;
