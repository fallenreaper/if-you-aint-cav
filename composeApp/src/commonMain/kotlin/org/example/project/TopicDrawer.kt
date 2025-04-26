package org.example.project

import androidx.compose.material.TopAppBar
//import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import org.jetbrains.compose.ui.tooling.preview.Preview

enum class AppRoutes(title: String) {
    Topics(title="Topics"),
    FundamentalsOfRecon(title = "Fundamentals of Reconnaissance"),
    FundamentalsOfSecurity(title="Fundamentals of Security")
}


@Composable
@Preview
fun TopicDrawer () {

//    val mediumTopAppBarColors = TopAppBarDefaults.mediumTopAppBarColors()
    TopAppBar(
        title = { AppRoutes.Topics },
//        colors = mediumTopAppBarColors
    )
}