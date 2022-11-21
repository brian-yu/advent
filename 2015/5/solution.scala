def isNice(s: String): Boolean =
  var hasRepeated = false
  var vowelCount = 0

  for ((char, i) <- s.zipWithIndex)
    val prev = if i >= 1 then s(i - 1) else None

    if ("aeiou".indexOf(char) >= 0)
      vowelCount += 1

    if (char == prev)
      hasRepeated = true
    
    s"$prev$char" match
      case "ab" => return false
      case "cd" => return false
      case "pq" => return false
      case "xy" => return false
      case _ =>
  
  return hasRepeated && vowelCount >= 3

def isNiceV2(s: String): Boolean =
  var hasRepeatedChar = false
  var hasRepeatedPair = false

  var pairsSeenSoFar = Map[String, Int]()

  for ((char, i) <- s.zipWithIndex)
    val prev = if i >= 1 then s(i - 1) else None
    val two_prev = if i >= 2 then s(i - 2) else None

    if (char == two_prev)
      hasRepeatedChar = true
    
    val pair = s"$prev$char"
    if (pairsSeenSoFar.contains(pair) && pairsSeenSoFar(pair) < i - 1)
      hasRepeatedPair = true
    else if (!pairsSeenSoFar.contains(pair))
      pairsSeenSoFar += (pair -> i)
  
  return hasRepeatedPair && hasRepeatedChar
  

@main def main =
  val source = scala.io.Source.fromFile("input.txt")
  val strings = try source.getLines.toArray finally source.close()

  println(strings.count(isNice))
  println(strings.count(isNiceV2))
