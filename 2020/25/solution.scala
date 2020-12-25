def apply_transform(value: Long, subject: Long): Long =
  (value * subject) % 20201227

def transform(subject: Long, loop_size: Int): Long =
  var value: Long = 1
  for (_ <- Range(0, loop_size))
    value = apply_transform(value, subject)
  value

def find_loop_size(subject: Int, public_key: Int): Int =
  var loop_size = 0
  var value: Long = 1

  while (value != public_key)
    value = apply_transform(value, subject)
    loop_size += 1
  
  loop_size

@main def main =
  val source = scala.io.Source.fromFile("input.txt")
  val Array(card_public_key, door_public_key) = try
    source.getLines.toArray.map(_.toInt)
  finally
    source.close()

  val card_loop_size = find_loop_size(7, card_public_key)
  val door_loop_size = find_loop_size(7, door_public_key)

  println(transform(door_public_key, card_loop_size))
  println(transform(card_public_key, door_loop_size))
