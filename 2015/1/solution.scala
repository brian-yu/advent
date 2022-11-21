
def findPosition(s: String): Option[Int] =
    var open = 0
    var closed = 0

    for ((elem, i) <- s.zipWithIndex)
        elem match
            case '(' => open += 1
            case ')' => closed += 1
        
        if (open == closed - 1)
            return Some(i + 1)

    return None

@main def main =
    val source = scala.io.Source.fromFile("input.txt")
    val lines = try source.mkString finally source.close()

    println(lines.count(_ == '(') - lines.count(_ == ')'))

    
    
    println(findPosition(lines))

    
            