import threading
import time

cake='''

                                                                                                   
                                                 🕉                               
                                            ,    (%    .                       
                                            ..   %@.   ,                    
                                            #*  ,@@(   .#                                         
                                         ,@@#   (@@&    @@.                   
                                        &@@%    %@@@/   @@@%                   
                                      #@@@@     @@@@@    %@&@#             
                                    %@&&@#     @@@@@@@    &@./@(              
                                  *@@*/@(      (@@@@@(     (@( %@/           
                                 %@@ /@(       #%&&%&       #@# &@&       
                                @@@/ %@*     ,&@@@@@@&,      @@*(@@@          
                               *@@@@@@@# #@@@&  ,@@(  @@@@% #@@@@@@@/        
                                \&@@@@@&    *🕉🕉/    @@@@@@@@@@@@@/          
                                  \@@@@@@@@@@@#&@@@&@@@@@@@@@@@@@/                 
                                    \@@@@@@@@@@&   *@@@@@@@@@@@/                          
                                       🕉🕉🕉🕉🕉🕉🕉🕉🕉🕉🕉🕉🕉🕉                         
                                              /@@.&&\                     
                                             /@@@@@@@@\                    
                                           %@@@@    &@@@,                     
                                         /@@@(       .@@.             
                                         .%@#    .    @@,                 
                                              *.    (@@@/                        
                                             (     #@@@/                 
                                         ..#   .%@@@(                 
                                       (,%  .%@@&%%%@@@@@@@&                 
                                     %*%  .@@(       .@@@@@@@,                  
                                   ,@(@  #@/       #@@&.  .@%&(                  
                                   &@#.  @.     ,@@@,      *@ @                   
                                   @&%   *.   .@@&         (% @.            
                                   (@%@      #@@          %& %                
                                    /@@@&.  @@@        ,&@@@%              
                                      /@@@@@@@#((##&@@@@@&*                   
                                         .#&@@@@@@@@@&,                         
                                            @%   ,@@@                             
                                             %#  .@@.                            
                                               /(.@#                          
                                                .@*                          
                                                .@.                       
                                                 @                          
                                                 #
                                                 /                             
                                                 /
                                                 .
                                                 .
'''
def task1():
    for letter in cake:
        time.sleep(0.01)
        print(letter,end=")
ti = threading.Thread(target=task1,name='t1')

t1.start()

