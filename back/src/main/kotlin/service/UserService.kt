package com.cybergames.service

import com.cybergames.entities.User
import com.cybergames.repository.UserRepository
import com.cybergames.service.mail.EmailSenderService
import org.springframework.stereotype.Service

@Service
class UserService( val userRepository: UserRepository,
                   val mailService: EmailSenderService) {

    fun create(user: User): Long? {
        val persistedUser =  userRepository.save(user)
        return persistedUser.id
    }

    fun delete(id : Long){
        userRepository.deleteById(id)
    }

    fun findAll() : MutableIterable<User> {
        return userRepository.findAll()
    }
}