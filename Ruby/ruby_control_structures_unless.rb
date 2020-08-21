def scoring(array)
    # array.reject(&:is_admin?).each(&:update_score)
    array.each do |user| 
        unless user.is_admin?
            user.update_score
        end
        # user.update_score unless user.is_admin?
    end
end
