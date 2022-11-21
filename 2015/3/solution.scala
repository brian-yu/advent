@main def main =
  val source = scala.io.Source.fromFile("input.txt")
  val directions = try source.getLines.mkString finally source.close()

  var position = (0, 0)
  var houses = Set(position)

  for (direction <- directions)
    position = direction match
      case '<' => (position._1 - 1, position._2)
      case '>' => (position._1 + 1, position._2)
      case '^' => (position._1, position._2 + 1)
      case 'v' => (position._1, position._2 - 1)
      
      houses += position
      
  println(houses.size)

  var santa = (0, 0)
  var roboSanta = (0, 0)
  houses = Set(santa, roboSanta)

  for ((direction, i) <- directions.zipWithIndex)
    var position = if (i % 2 == 0)
      santa
    else
      roboSanta

    position = direction match
      case '<' => (position._1 - 1, position._2)
      case '>' => (position._1 + 1, position._2)
      case '^' => (position._1, position._2 + 1)
      case 'v' => (position._1, position._2 - 1)
      
      houses += position
    
    if (i % 2 == 0)
      santa = position
    else
      roboSanta = position
      
  println(houses.size)
