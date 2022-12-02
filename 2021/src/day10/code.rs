use crate::Solution;
use std::fs;

pub struct Day {
    pub input_path: String,
}

fn find_invalid_token(s: &str) -> Option<char> {
    let mut stack: Vec<char> = vec![];
    for char in s.chars() {
        if is_opening_char(char) {
            stack.push(char);
        } else if *stack.last().unwrap() == matching_char(char) {
            stack.pop();
        } else {
            return Some(char);
        }
    }
    None
}

fn is_opening_char(char: char) -> bool {
    matches!(char, '(' | '[' | '{' | '<')
}

fn matching_char(char: char) -> char {
    match char {
        '(' => ')',
        '[' => ']',
        '{' => '}',
        '<' => '>',
        ')' => '(',
        ']' => '[',
        '}' => '{',
        '>' => '<',
        char => panic!("Oops. Invalid token: {}", char),
    }
}

fn is_corrupted(line: &str) -> bool {
    find_invalid_token(line).is_some()
}

fn find_completing_sequence(line: &str) -> String {
    let mut stack: Vec<char> = vec![];
    for char in line.chars() {
        if is_opening_char(char) {
            stack.push(char);
        } else if *stack.last().unwrap() == matching_char(char) {
            stack.pop();
        }
    }

    let mut sequence: Vec<char> = vec![];
    while let Some(char) = stack.pop() {
        sequence.push(matching_char(char));
    }

    sequence.iter().collect()
}

fn score_sequence(sequence: &str) -> usize {
    let mut score = 0;
    for char in sequence.chars() {
        score *= 5;
        score += match char {
            ')' => 1,
            ']' => 2,
            '}' => 3,
            '>' => 4,
            other => panic!("Oops. Invalid token: {}", other),
        }
    }

    score
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        let mut score = 0;
        for line in input.trim().split('\n') {
            if let Some(token) = find_invalid_token(line) {
                // println!("Invalid token for {} is {}", line, token);
                score += match token {
                    ')' => 3,
                    ']' => 57,
                    '}' => 1197,
                    '>' => 25137,
                    char => panic!("Oops. Invalid token: {}", char),
                }
            }
        }
        println!("{}", score);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        let incomplete_lines = input.trim().split('\n').filter(|line| !is_corrupted(line));

        let mut scores = vec![];

        for line in incomplete_lines {
            let seq = find_completing_sequence(line);
            println!("{} -> {} -> {}", line, seq, score_sequence(&seq));
            scores.push(score_sequence(&seq));
        }

        scores.sort();
        println!("{}", scores[scores.len() / 2]);
    }
}
