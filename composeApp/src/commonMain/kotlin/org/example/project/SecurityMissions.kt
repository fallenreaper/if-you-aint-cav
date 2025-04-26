package org.example.project

import androidx.compose.foundation.gestures.scrollable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.Divider
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.TextUnit
import androidx.compose.ui.unit.dp
import org.jetbrains.compose.ui.tooling.preview.Preview


@Composable
@Preview
fun SecurityMissions(content: Array<Pair<String,String>>) {
    val mod = Modifier.fillMaxWidth(1f)
    MaterialTheme {
        Column(modifier = Modifier.padding(all=20.dp).verticalScroll(rememberScrollState())) {
            Text("Security Missions",
                textAlign = TextAlign.Center,
                fontWeight = FontWeight.Bold,
                modifier = mod)
            Divider()

            content.forEach {
                (name,desc) ->
                    Text(name, textAlign = TextAlign.Center, fontWeight = FontWeight.Bold, modifier = mod)
                    Text(desc)
                    Divider()
            }

        }
    }
}