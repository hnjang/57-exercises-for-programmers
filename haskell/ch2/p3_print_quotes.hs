main = do
    let first_s = "What is the quote? "
    let second_s = "These aren\'t the droids you\'re looking for."
    let third_s = "Who said it?"
    let concat = first_s ++ "\n" ++ second_s ++ "\n" ++ third_s
    putStrLn (concat)
    name <- getLine
    putStrLn (name ++ ", says, \"" ++ second_s ++ "\"")
