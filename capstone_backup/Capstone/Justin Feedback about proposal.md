## proposal comments
<span style="color:lime"> Overall thoughts about your project are in green. </span>
<span style="color:firebrick"> *Specific comments about process/ideas are in red* </span>
============

<span style="color:lime"> overall i think this is a good project. there are a few things to iron out (i think your model can be simplified) and i would move a few of your items to a "nice to have, but will do after MVP works" list. also, instead of focusing on node, simplify things by focussing on using javascript in the browser first. if you need to bring in some functionality only node can provide, that's fine, but try to avoid using it because it does kind of overcomplicate things. </span>


<span style="color:firebrick">as for your list of tasks:</span>
1. Allow new users (lenders or borrowers) to register accounts. 
2. Allow users (borrowers or lenders) to Logon and Logoff. 
3. Allow borrowers to search equipment from the equipment database for renting. 
4. <span style="color:firebrick"> *allow borrowers to request an equipment for rent.* </span>
5. Allow lenders to upload equipment to the equipment database for leasing. 
5. <span style="color:firebrick">Provide suggested leasing price based on the existing market </span>
6. <span style="color:firebrick">Allow lenders to accept the rental request. </span>
7. Create Equipment database table that shows a list of equipment for rent.
8. Create Transaction database table that shows all current and historical transactions.
9. Create User database table that contain user's profile information.

<span style="color:firebrick">depending on how you do this, requesting equipment and accepting the request could be pretty intensive for an initial stab at the project. providing leasing information based on existing market will require you to tie into some database/api to get that information. what do you do if that api/databse has an outage? depending on how much time you can work on this outside of class, i think these are two aspects that should be moved to a "nice to have, but will do after MVP" section. i like the ideas, but i think they'd take too much time and would like to see you get a simpler MVP in place first before tackling them</span>


<span style="color:firebrick">regarding your models, i think your model could be simplified a little bit. let's talk about that this week. i think you can just have users and set them up to be both borrowers and renters. they can have a list of tools or not. no need to create specific borrowers and renters. this is just an initial thought though.
