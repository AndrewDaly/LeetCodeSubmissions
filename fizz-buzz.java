class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> retval = new ArrayList<String>();
        String FizzBuzz = "FizzBuzz";
        String Fizz = "Fizz";
        String Buzz = "Buzz";
        for(int i = 0; i<= n; i++){
            if(i%3==0 && i%5==0 && i>4){
                //place fixxbuxx
                retval.add(FizzBuzz);
                continue;
            }
            if(i%3==0 && i>2){
                retval.add(Fizz);
                //place fixx
                continue;
            }
            if(i%5==0 && i>4){
                retval.add(Buzz);
                //place buzz
                continue;
            }
            else{
                retval.add(String.valueOf(i));
                //place i
                continue;
            }
        }
        retval.remove(0);
        return retval;
        
    }
}
