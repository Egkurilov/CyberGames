package com.cybergames

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class ServerKt {
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            runApplication<ServerKt>(*args);
        }
    }
}
