package com.cybergames.controller

import com.cybergames.entities.User
import com.cybergames.service.UserService
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import javax.websocket.server.PathParam

@RestController
@RequestMapping
class UserController(val userService: UserService) {
    @PostMapping("/user/add")
    fun add(@RequestBody user : User) : ResponseEntity<Long>{
        return ResponseEntity.ok(userService.create(user))
    }

    @DeleteMapping("/user/{id}")
    fun delete(@PathParam("id") id : Long) : ResponseEntity<Long>{
        userService.delete(id)
        return ResponseEntity.ok(id)
    }

    @GetMapping("/user")
    fun all() : ResponseEntity<MutableIterable<User>>{
        return ResponseEntity.ok(userService.findAll())
    }
}