main = do
    putStrLn "What is the input string?"
    name <- getLine
    putStrLn (name ++ " has " ++ show(length name) ++ " characters.")
