package com.cybergames.service

import com.cybergames.entities.User
import com.cybergames.repository.UserRepository
import org.springframework.stereotype.Service

@Service
class UserService( val userRepository: UserRepository) {
    fun create(user: User): Long? {
        return userRepository.save(user).id
    }

    fun delete(id : Long){
        userRepository.deleteById(id)
    }

    fun findAll() : MutableIterable<User> {
        return userRepository.findAll()
    }
}