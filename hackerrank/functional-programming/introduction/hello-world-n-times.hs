hello_worlds n = sequence_ [putStrLn "Hello World" | i <- [1..n]]

main = do
   n <- readLn :: IO Int
   hello_worlds n