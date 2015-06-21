module Main where

gcd' :: Integral a => a -> a -> a
gcd' n m =  gcd' (abs n) (abs m) where
  gcd' n 0  =  n
  gcd' n m  =  gcd' m (n `rem` m)

main = do
  input <- getLine
  print . uncurry gcd' . listToTuple . convertToInt . words $ input
 where
  listToTuple (x:xs:_) = (x,xs)
  convertToInt = map (read :: String -> Int)