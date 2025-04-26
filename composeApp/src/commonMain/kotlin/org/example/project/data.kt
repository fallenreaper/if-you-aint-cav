package org.example.project

class data() {

    companion object {
        val content: Map<String,Array<Pair<String,String>>> = mapOf(
            Pair("securityMissions", arrayOf(
                Pair("Screen", "4-22. A screen is a security task that scout platoons conduct to provide early warning to" +
                        "the protected force and report information related to a commander’s PIR. Within its" +
                        "04 December 2019 ATP 3-20.98 4-7" +
                        "capabilities and based upon the higher commander’s guidance, the scout platoon" +
                        "conducts counterreconnaissance to destroy or repel enemy reconnaissance forces." +
                        "Screen tasks are defensive in nature and prevent enemy observation of the protected" +
                        "force. Scout platoons conduct screens to the front, flanks, or rear of a stationary friendly" +
                        "force, and to the flanks or rear of a moving friendly force. Scout"),
                Pair("Guard", "4-99. Guard is a security task to protect the main body by fighting to gain time while" +
                        "also observing and reporting information and preventing enemy ground observation of" +
                        "and direct fire against the main body. Units conducting a guard mission cannot operate" +
                        "independently because they rely upon fires and functional and multifunctional support" +
                        "assets of the main body. BCT commanders might assign a guard mission when they" +
                        "expect contact or has an exposed flank that requires greater protection than a screen can" +
                        "provide. The guard force conducts reconnaissance, attacks, defends, and delays as" +
                        "necessary to provide reaction time and maneuver space to the protected force. There are" +
                        "three types of guard missions: advance guard, flank guard, and rear guard. Additionally," +
                        "a commander may assign a guard mission to protect a stationary or moving force. (Refer" +
                        "to FM 3-98 and ATP 3-20.97 for greater detail on guard missions)."),
                Pair("Cover", "4-101. Cover is a security task that is a self-contained force that is capable of operating" +
                        "independently of the main body to allow early development of the situation, deceive," +
                        "disorganize, and destroy enemy forces. The covering force protects the main body by" +
                        "fighting to gain time while also observing and reporting information and preventing" +
                        "enemy ground observation of and direct fires against the main body. The key distinction" +
                        "to remember is unlike the screen or guard, cover is tactically self-contained, meaning," +
                        "because the covering force or portions of it often engage with enemy forces, it must have" +
                        "substantial combat power and sustainment resources to engage the enemy and still" +
                        "accomplish its mission. In addition, a covering force accomplishes all the tasks of screen" +
                        "or guard. Cover force is generally conducted by a reinforced BCT-sized element. (Refer" +
                        "to FM 3-98 for a better understanding of cover.)")
            )),

            )
        fun getSecurityMissions(): Array<Pair<String, String>> {
            return data.content["securityMissions"]!!;
        }
    }
}