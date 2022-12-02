use crate::Solution;
use std::{fs, str::FromStr};

pub struct Day {
    pub input_path: String,
}

enum Play {
    Rock,
    Paper,
    Scissors,
}

enum Outcome {
    Win,
    Lose,
    Draw,
}

struct Match {
    player: Play,
    other: Play,
}

#[derive(Debug, Clone)]
struct ParseError;

impl FromStr for Match {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        if let Some((other_s, player_s)) = s.split_once(' ') {
            return Ok(Match {
                player: match player_s {
                    "X" => Play::Rock,
                    "Y" => Play::Paper,
                    "Z" => Play::Scissors,
                    _ => panic!("Invalid char"),
                },
                other: match other_s {
                    "A" => Play::Rock,
                    "B" => Play::Paper,
                    "C" => Play::Scissors,
                    _ => panic!("Invalid char"),
                },
            });
        }

        Err(ParseError)
    }
}

impl Match {
    fn outcome(player: &Play, other: &Play) -> Outcome {
        match (player, other) {
            (Play::Rock, Play::Rock) => Outcome::Draw,
            (Play::Rock, Play::Paper) => Outcome::Lose,
            (Play::Rock, Play::Scissors) => Outcome::Win,
            (Play::Paper, Play::Rock) => Outcome::Win,
            (Play::Paper, Play::Paper) => Outcome::Draw,
            (Play::Paper, Play::Scissors) => Outcome::Lose,
            (Play::Scissors, Play::Rock) => Outcome::Lose,
            (Play::Scissors, Play::Paper) => Outcome::Win,
            (Play::Scissors, Play::Scissors) => Outcome::Draw,
        }
    }

    fn needed_outcome(&self) -> Outcome {
        match &self.player {
            Play::Rock => Outcome::Lose,
            Play::Paper => Outcome::Draw,
            Play::Scissors => Outcome::Win,
        }
    }

    fn score(&self) -> u32 {
        let outcome_score = match Match::outcome(&self.player, &self.other) {
            Outcome::Win => 6,
            Outcome::Draw => 3,
            Outcome::Lose => 0,
        };

        let play_score = match &self.player {
            Play::Rock => 1,
            Play::Paper => 2,
            Play::Scissors => 3,
        };

        outcome_score + play_score
    }

    fn score_2(&self) -> u32 {
        let needed_outcome = self.needed_outcome();

        let needed_play = match (&self.other, &needed_outcome) {
            (Play::Rock, Outcome::Lose) => Play::Scissors,
            (Play::Rock, Outcome::Draw) => Play::Rock,
            (Play::Rock, Outcome::Win) => Play::Paper,
            (Play::Paper, Outcome::Lose) => Play::Rock,
            (Play::Paper, Outcome::Draw) => Play::Paper,
            (Play::Paper, Outcome::Win) => Play::Scissors,
            (Play::Scissors, Outcome::Lose) => Play::Paper,
            (Play::Scissors, Outcome::Draw) => Play::Scissors,
            (Play::Scissors, Outcome::Win) => Play::Rock,
        };

        let outcome_score = match &needed_outcome {
            Outcome::Lose => 0,
            Outcome::Draw => 3,
            Outcome::Win => 6,
        };

        let play_score = match &needed_play {
            Play::Rock => 1,
            Play::Paper => 2,
            Play::Scissors => 3,
        };

        outcome_score + play_score
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let score: u32 = input
            .trim()
            .split('\n')
            .map(|line| line.parse::<Match>().unwrap().score())
            .sum();

        println!("{}", score);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let score: u32 = input
            .trim()
            .split('\n')
            .map(|line| line.parse::<Match>().unwrap().score_2())
            .sum();

        println!("{}", score);
    }
}
