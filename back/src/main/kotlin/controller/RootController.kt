package main.kotlin.controller

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping

@Controller

class RootController {
    @GetMapping("/test")
    fun test(): String {
        return "ok"
    }
}