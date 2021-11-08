package com.cybergames.controller

import com.cybergames.entities.User
import com.cybergames.service.UserService
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.DeleteMapping
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import javax.websocket.server.PathParam

@Controller
class UserController(val userService: UserService) {
    @PostMapping("/users/add")
    fun add(@RequestBody user : User) : ResponseEntity<Long>{
        return ResponseEntity.ok(userService.create(user))
    }

    @DeleteMapping("/users/{id}")
    fun delete(@PathParam("id") id : Long) : ResponseEntity<Long>{
        userService.delete(id)
        return ResponseEntity.ok(id)
    }

    @GetMapping("/users")
    fun all() : ResponseEntity<MutableIterable<User>>{
        return ResponseEntity.ok(userService.findAll())
    }
}